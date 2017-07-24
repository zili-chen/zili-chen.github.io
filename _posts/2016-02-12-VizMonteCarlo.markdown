---
layout: default
title:  VizMonteCarlo
date:   2016-05-12 17:50:00
categories: blog
---

# Viz  Monte Carlo

This is part of my course project for undergraduate course *Computational condensed matter physics*.

In short, Monte Carlo methods is one reflection of **the Law of Large Numbers**, which indicates that **a large number of randomness could present deterministic behaviour in principle**. For example, from kinetic theory of gases, we  know that a gas is a great amount of particles, whose motions are in nature stochastic, due to colisions with each other and with the walls of container. However, a gas may have stable macroscopic properties, such as pressure, temperature.

Monte Carlo methods are widely used in all computation-related scientific areas. Two common usages are simulation and integration.

<iframe src= "../../../../project/VizMonteCarlo/VizMonteCarlo.html"  scrolling="no" style="height:100%;width:100%" frameBorder="0"> </iframe>

The above figure visulizes a classical application of Monte Carlo method to computing $$\pi$$. 

Denote the indicator random variable of the sector in the figure by $$X$$ and its expectation $$\mu = \frac{\pi}{4}$$. We perform independent experiments $$n$$ times. $$\pi$$ can be approximated as

$$\begin{align}\pi  &=  4 \times \mathbb{E}(X)\\ &= \frac{4}{n} \times \mathbb{E}(X_1 + \cdots X_n) \\&\approx 4 \times \frac{\#\{ \mbox{points inside circle}\}}{\#\{ \mbox{points inside circle}\} + \#\{ \mbox{points outside circle}\}} \end{align} $$

Then the standard deviation of the approximation error can be bounded above by $$\sigma_{error} = \frac{4}{\sqrt{n}} \times \sigma_X = \frac{4}{n} \sqrt{p(1-p)} \le\frac{2}{\sqrt{n}}$$ , as illustrated by the boundary of two swept areas in the above figure.

Despite the fact that Monte Carlo method is free from **the Curse of Dimensionality**, from error estimate, we know that the rate of convergence (in probablistic sense) Monte Carlo method is quite slow, in the order of $$O(n^{-\frac{1}{2}})$$, which migth be too slow in many practial applications.













