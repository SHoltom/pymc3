import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymc3
#import scipy.stats as stats

plt.style.use("ggplot")
# Parameter values for prior and analytic posterior
n = 50
z = 10
alpha = 12
beta = 12
alpha_post = 22
beta_post = 52

# How many iterations of the Metropolis
# algorithm to carry out for MCMC
iterations = 100000
