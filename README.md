# FakeNodes
Python code for Fake Nodes interpolation approach.

![fig1](runge_interp.png)

Fake nodes approach give the possibility to obtain a better interpolation without getting new samples!

![fig2](runge_lebesgue.png)

Fake nodes is a new approach for interpolation, allowing to obtain more stable and more precise interpolation **without the need of resampling**. 

The method works in a simple way. Given:

* a training set of $n$ samples $X_n$,
* the corresponding output $Y_n = f(X_n)$,
* a test set $X$,

we have to compute the predicted output $Y \approx f(X)$ by interpolation.

Instead of using directly the intepolation of the pairs $(X_n,Y_n)$, we propose to compute $\Pi$, the interpolant of $(S(X_n),Y_n)$, being $S$ a properly chosen (injective) mapping. The predicted output wil be $\Pi(S(X))$.

In the next notebooks we will show the treatment of two classical phenomena in polynomial interpolation: the [Runge effect](Runge.ipynb) effect and the [Gibbs effect](Gibbs.ipynb) effect.

To use this work in any scientific report or publication, please cite:

 * S. De Marchi, F. Marchetti, E. Perracchione, D. Poggiali, *Polynomial Interpolation at Fake Nodes*