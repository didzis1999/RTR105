Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/Monte-Carlo.py', 'random': <module 'numpy.random' from '/usr/lib/python2.7/dist-packages/numpy/random/__init__.pyc'>, '__package__': None, 'sys': <module 'sys' (built-in)>, '__name__': '__main__', '__doc__': None}
>>> prin(random._doc_)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    prin(random._doc_)
NameError: name 'prin' is not defined
>>> print(random.__doc_)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(random.__doc_)
AttributeError: 'module' object has no attribute '__doc_'
>>> print(random.__doc__)

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> print (random.uniform.__doc__)

        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        Parameters
        ----------
        low : float, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float
            Upper boundary of the output interval.  All values generated will be
            less than high.  The default value is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : ndarray
            Drawn samples, with shape `size`.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, normed=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

        
>>> random.uniform(0,1,5)
array([ 0.93558171,  0.78851753,  0.38498453,  0.81490301,  0.81637083])
>>> random.uniform(0,0.1,10)
array([ 0.03825044,  0.01823565,  0.00155482,  0.0061996 ,  0.07833588,
        0.08669867,  0.08804308,  0.03323604,  0.09782884,  0.06571653])
>>> for i in rang(10):
	int(random.uniform(0,100))

	

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for i in rang(10):
NameError: name 'rang' is not defined
>>> for i in rang(10):
	int(random.uniform(0,100))


Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for i in rang(10):
NameError: name 'rang' is not defined
>>> type(random.uniform(0,100))
<type 'float'>
>>> random.unifrom(0,1,5)

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    random.unifrom(0,1,5)
AttributeError: 'module' object has no attribute 'unifrom'
>>> type(random.uniform(0,100))
<type 'float'>
>>> random.unifrom(0,1,5)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    random.unifrom(0,1,5)
AttributeError: 'module' object has no attribute 'unifrom'
>>> random.seed(1)
>>> random.unifrom(0,1,5)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    random.unifrom(0,1,5)
AttributeError: 'module' object has no attribute 'unifrom'
>>> print(random.uniform(0,1,10))
[  4.17022005e-01   7.20324493e-01   1.14374817e-04   3.02332573e-01
   1.46755891e-01   9.23385948e-02   1.86260211e-01   3.45560727e-01
   3.96767474e-01   5.38816734e-01]
>>> print(random.seed.__doc__)

        seed(seed=None)

        Seed the generator.

        This method is called when `RandomState` is initialized. It can be
        called again to re-seed the generator. For details, see `RandomState`.

        Parameters
        ----------
        seed : int or array_like, optional
            Seed for `RandomState`.
            Must be convertible to 32 bit unsigned integers.

        See Also
        --------
        RandomState

        
>>> random.seed(1)
>>> random.unifrom(0,1,5)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    random.unifrom(0,1,5)
AttributeError: 'module' object has no attribute 'unifrom'
>>> random.uniform(0,1,5)
array([  4.17022005e-01,   7.20324493e-01,   1.14374817e-04,
         3.02332573e-01,   1.46755891e-01])
>>> random.uniform(0,1,5)
array([ 0.09233859,  0.18626021,  0.34556073,  0.39676747,  0.53881673])
>>> random.uniform(0,1,5)
array([ 0.41919451,  0.6852195 ,  0.20445225,  0.87811744,  0.02738759])
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 27, in <module>
    elif x:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 27, in <module>
    elif x:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 27, in <module>
    elif x:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
[20, 16, 23, 17, 24]
100
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

================= RESTART: /home/user/RTR105/Monte-Carlo.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/Monte-Carlo.py", line 50, in <module>
    S_nezinaamais = 1. * S_zinaamais * N1/N
NameError: name 'N1' is not defined
>>> 
================= RESTART: /home/user/RTR105/Monte-Carlo.py =================
12.38
>>> 
