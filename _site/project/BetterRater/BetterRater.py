import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture as gmm
import names
import pyecharts as pe
import csv

def generate_csvfile(filepath, n_samples):
	'''
	This function simulates a rating csv file, with header 'Name', 'Average Score', 'Standard Deviation',
	and random generates n_sample records.

	parameters:
		filepath: string, the path of generated csv file
		n_samples: int, number of generated records

	return:
		None
	'''
	def generate_staff(n_staff, mean, cov):
		group = np.random.multivariate_normal(mean, cov, n_staff)
		group = np.minimum(group, 5.0)
		group = np.maximum(group, 0.0)

		for i in range(len(group)):
			if group[i][0] == 5.0 and group[i][1] != 0.0:
				group[i][1] = 0.0
			elif group[i][0] != 5.0 and group[i][1] == 0.0:
				group[i][0] = round(group[i][0])
		
		return group

	mean1, cov1, mean2, cov2 = [4.6, 0.2], [[0.1, 0.05],[0.05, 0.1]], [3.8, 0.6], [[0.2, 0],[0, 0.2]]
	group1 = generate_staff(n_samples/2, mean1, cov1)
	group2 = generate_staff(n_samples/2, mean2, cov2)
	group = np.vstack([group1, group2])
	
	with open(filepath, 'w') as csvfile:
		fieldnames = ['Name', 'Average Score', 'Standard Deviation']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
		for i in range(len(group)):
			writer.writerow({'Name': names.get_first_name(),
							 'Average Score': group[i][0],
							 'Standard Deviation': group[i][1]})


def select(rating):
	'''
	This function selects bad raters from rating dataframe and the update labels for each staff.

	Parameters:
		rating: pandas dataframe, stores rating information

	Return:
		updated_label: np.array, updated label information
	'''
	index = rating['Label'] == 1
	X_train = [[row['Average Score'], row['Standard Deviation']] for _, row in rating.loc[index].iterrows()]
    
	clf = gmm(n_components=2, covariance_type='diag', random_state=0)
	clf.fit(X_train)
	mean0, mean1 = clf.means_
	new_labels = clf.predict(X_train)
    
	point = np.array([5.0, 0.0])
	if np.linalg.norm(mean0 - point) < np.linalg.norm(mean1 - point):
		new_labels = 1.0 - new_labels  # make sure staff with label 1 are bad raters

	rating.loc[index, 'Label'] = new_labels
	return rating


def effectscatter(rating):
    	index0 = rating['Label'] == 0
    	index1 = rating['Label'] == 1
    	
    	point = np.array([5.0, 0.0])

    	es = pe.EffectScatter("Rating", title_pos='center', width=1200, height=600)
    	for _, row in rating.loc[index1].iterrows():
			distance = np.linalg.norm(np.array([row['Average Score'], row['Standard Deviation']]) - point)
			size = 20.0  / (distance + 1.0)
			es.add(row['Name'], [row['Average Score']], [row['Standard Deviation']], sybol_size=size)
    	for _, row in rating.loc[index0].iterrows():
			distance = np.linalg.norm(np.array([row['Average Score'], row['Standard Deviation']]) - point)
			size = 10.0  / (distance + 1.0)
			es.add(row['Name'], [row['Average Score']], [row['Standard Deviation']], symbol_size=size, effect_scale=0)
    	es.add("", [], [], xaxis_name='Average Score', yaxis_name='Standard Deviation', is_legend_show=False) 
    	es.render()
    	return es

if __name__ == "__main__":
    filepath = "sample.csv"
	
    rating = pd.read_csv(filepath)
    rating['Label'] = pd.Series(1, index=rating.index)
    
    select(rating)
    effectscatter(rating)



    

