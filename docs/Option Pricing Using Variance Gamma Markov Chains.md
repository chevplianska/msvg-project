# Option Pricing Using Variance Gamma Markov Chains 

MIKHAIL KONIKOV<br>Department of Mathematics, University of Maryland, College Park, MD 20742<br>DILIP B. MADAN<br>Robert H. Smith School of Business, University of Maryland, College Park, MD 20742

Received December 27, 2000; Revised October 3, 2001


#### Abstract

This paper proposes a Markov Chain between homogeneous Lévy processes as a candidate class of processes for the statistical and risk neutral dynamics of financial asset prices. The method is illustrated using the variance gamma process. Closed forms for the characteristic function are developed and this renders feasible, maximum likelihood estimation and option pricing. The statistical and risk neutral process is fit to data on time series and option prices respectively. It is observed in the statistical estimation that single names have an average period of 4 to 6 months in a state while this reduces to one month for indices. Risk neutrally there is generally a low probability of a move to a state with higher moments. In some cases this is reversed.


The task of modeling equity option prices is quite challenging, notwithstanding the simplicity of the Black-Merton-Scholes option pricing formula. On a typical underlying, for example the S\&P 500 index, there are some 200 option prices ranging across 20 strikes and 10 maturities at any instant, to be consistently explained by the prospective model: And this hopefully consistently through calendar time as well. From this perspective the simplicity of the Black and Scholes (1973), Merton (1973) approach is unrealistically glaring. Were that theory to be empirically valid then the information content of the observed 200 prices would have an effective dimension of one, as one may perfectly predict the other 199 prices from any one of them. Such a dimensional reduction is an unrealistic expectation. Market experience concurs, as is evidenced by the practice of computing implied volatilities that vary with both strike and maturity.

At the other extreme from the one dimensional Black-Merton-Scholes model lie the non-parametric approaches. These methods implicitly accept that the dimensional content of the surface can not be reduced at all. They then model the implied volatility surface as evolving in the doubly infinite dimensional space of volatilities indexed by strike and maturity. The information content of option prices being essentially one-to-one with set of these prices. For example, local volatility models fall in this category, attempting to infer the function of local volatilities varying with time and the level of the spot price, from the potential two dimensional continuum of option prices for all strikes and maturities as described in Dupire (1994) or Derman and Kani (1998).

Parametric models occupy the intermediate domain and attempt to reduce the information content of option prices dimensionally to the number of parameters of the model. Such models include the Merton (1976) jump diffusion model, the Heston (1993) stochastic volatility model, the combination called stochastic volatility with jumps studied for example in Bates (1996) and Bakshi, Cao and Chen (1997), and the more recent infinite activity Lévy process models studied in Eberlein, Keller and Prause (1998) or the normal inverse Gaussian studied by Barndorff-Nielsen (1998) the variance gamma studied in Madan, Carr and Chang (1998) or its extension in Carr, Geman, Madan and Yor (2000).

An issue of some importance in this regard is the status of the estimated parameters across calendar time. If they are constant then the model may be employed out-of-sample to forecast option prices consequent upon a movement of calendar time, the spot price or the level of latent variables like volatility in stochastic volatility models. However, this assumption of parametric constancy through calendar time has the implication that the time evolution of our 200 option prices is described adequately by a one or two dimensional Markov process. This two dimensional view of the surface dynamics is in our opinion as unrealistic as the one dimensional view of the static surface implied by the validity of the Black-Merton-Scholes model at a point of time.

We take the position that parameters estimated at a point of time from data on market prices synthesize important dimensions of information content in option prices, like the risk premia charged for a down move relative to a comparable up move or the premium charged for a large move relative to a small move independent of direction. These market premia can vary across time with the size and level of market interest in insuring against various moves. As a consequence we expect to see time variation in the parameters we estimate at a point of time and do not advocate the use of the estimated model out-ofsample. Our objective is to attempt to learn the dimension of the information content of option prices. In other words, time variation in what and how many parameters are critical to the dynamics of option prices.

In this regard we comment that we employ the methods of deriving option prices as conditional expectations of discounted final pay-offs under a measure on the space of paths taken at a point of time, to primarily enforce the absence of static arbitrage and elementary calendar spread arbitrages. In fact the stock price process we employ is a process of constant discounted expectation and in general, it is not a martingale. This is not a concern for as calendar time moves so will the parameters. The surface of option prices at a point of time is at the moment a rich enough object to be effectively synthesized.

This paper begins with two observations. The first is the recognition reported in Carr, Geman, Madan and Yor (2000), that in the presence of an infinite activity Lévy density characterizing the local motion of the stock there is little need to add a diffusion component to the model with the result that the price process is purely discontinuous. Jump diffusion models employ a diffusion component to describe the relatively large number of small price movements while an orthogonal Poisson process with a finite number of sizeable moves per unit time is used to model the large and relatively rarer moves.

Lévy processes that have been proposed and referenced above synthesize the study of moves of all sizes by first allowing for an infinite number of small moves and second requiring that arrival rates of moves of various sizes decline with the absolute value of the
size of the move. The infinite activity of moves near zero effectively substitutes for the diffusion component present in jump diffusion models. The decline in arrival rates as a function of the absolute size enforces the relative rarity of larger moves entirely across the size spectrum. In this way Lévy processes provide a more unified view of the price dynamics.

The theoretical case for Lévy type processes is made in Ané and Geman (2000) and Geman, Madan and Yor (2001). Essentially prices are seen as Brownian motions in an economic measure of time that is stochastically related to calendar time by a random process describing the time change. The number of units of economic time in a unit of calendar time is modeled as a positive random variable with the consequence that the time change is an increasing process. Such increasing time change processes have finite variation and in the presence of a martingale component are in many cases, purely discontinuous. As a consequence the price process becomes purely discontinuous.

Lévy processes are homogeneous processes of independent increments and as a result have volatility, skewness and kurtosis term structures that we present in this paper. It turns out that these term structures are not in accord with the data on market observed risk neutral moments. This observation renders this class of processes as incapable of explaining option prices across the maturity spectrum, notwithstanding their success across wide strike ranges at each maturity.

It is well known from numerous studies (see for example, Clark, (1973), Engle (1982), Nelson (1991), and Andersen, (1994)), that volatility has a clustering aspect modeled in Heston (1993) by employing a mean reverting process. For the Lévy processes, one may make stochastic the parameter calibrating the local quadratic variation and introduce mean reversion in its dynamic specification to develop the required clustering. For a study that pursues this approach we refer the reader to Carr, Geman, Madan and Yor (2001) and Barndorff-Nielsen and Shepard (1999).

This paper takes a simpler approach and builds clustering by employing a Markov chain that jumps between two homogeneous parametric specifications that calibrate to differing levels of volatility, as well as skewness and kurtosis. We are encouraged in taking this direction on observing how well a mixture of just two exponentials does in explaining interarrival times of daily market returns. For homogeneous processes this should be a single exponential, a fact strongly rejected by the data, yet the mixture of just two exponentials does remarkably well. We note that similar strategies have been pursued in the diffusion context by Duan, Popova and Ritchken (1999). We note additionally by way of comparison that the more traditional stochastic volatility models are like infinite state Markov chains where the states are represented by the positive continuum of the hidden volatility. It is in this respect that a two state Markov chain is a simpler object. Of course one could also consider three or more states at the cost of a considerable expansion of the parametric dimension and a rising complexity of the subsequent study of the time series of the estimated parameters.

We investigate this methodology for clustering the local moments in the context of the particularly tractable and relatively parsimonious variance gamma model. Needless to say, the exercise could be repeated with other base Lévy processes. The essential point is the demonstration that a homogeneous Lévy process by itself will not perform adequately across the maturity structure and our experience with the variance gamma suggests that

Markov chains in other Lévy processes may be equally successful, provided care is taken to employ infinite activity processes. We term our model a two-state variance gamma Markov model and employ the characteristic function methods used in Carr, Geman, Madan and Yor (2000) to make feasible both, maximum likelihood estimation of statistical parameters from time series data on returns, and risk neutral parameter estimation by non-linear least squares from data on option prices. We conclude that the Markov chain methodology is an attractive and tractable way to incorporate the phenomenon of clustering.

We recognize that models for the risk neutral dynamics are linked to the statistical dynamics by the property of equivalence. Essentially both probabilities assign different probabilities to sets of events but speak of the same set of events. Hence, if a two state Markov chain is to adequately represent the risk neutral dynamics it must be present in the effective description of the statistical process. The market prices of the moves in the underlying processes may differ from their relative frequency to an extent reflecting risk aversion in the economy but the same moves are relevant for both probabilities. These considerations motivate our statistical investigations, notwithstanding the associated complexities for portfolio analysis, a feature shared with the general incorporation of stochastic volatility.

An important aspect of studying both the statistical and risk neutral probabilities on the same underlying risks and in the same parametric class is the resulting ability to learn the nature of the way in which probabilities are changed. Within the class of homogeneous processes this question is addressed in some detail in Carr, Geman, Madan and Yor (2000). If one has to construct a risk profile on a derivatives book say one month out then one has to simulate the statistical process out that far and then the book of longer dated derivatives may be priced at the one month point by further simulating the statistical process to the maturities of the derivatives, but now also incorporating the measure change deduced from a simultaneous study of the two measures. These are important related issues but we leave the explicit construction of measure changes for this more delicate context to subsequent research. For further details on this problem we refer the reader to Elliott, Aggoun and Moore (1995).

In the statistical analysis we find that transition rates are significant, confirming the presence of two states. Likelihood ratio tests also reject the variance gamma in favor of the two-state variance gamma Markov model. For many single names the average time spent in the each of the two states ranges between four and six months and this drops interestingly for indices down to one month. Consistent with the rising term structure of statistical moments we observe that the current state tends to be one with the lower statistical moments with a transition to the higher states with higher moments.

From the analysis of the estimated risk neutral processes one notes that the model has a good ability to calibrate across strikes and maturities, sometimes attaining an average percentage error as low as $3 \%$ for over 5 maturities. For some single names, notably IBM and INTC we estimate a transition to quieter times though for the S\&P 500 index there is a small probability of transition to a state with high levels for the moments concerned.

The outline of the paper is as follows. Section 1 briefly describes the structure of Lévy processes to be employed and their primary properties and relevance to option pricing. In

Section 2 we establish the theoretical term structure patterns for volatility, skewness and kurtosis for Lévy processes or homogeneous processes of independent increments and we also document their departure from the data on S\&P500 options. Section 3 presents evidence demonstrating the ability of a mixture of two exponentials in explaining interarrival times. Section 4 develops closed forms for the characteristic function of the log price relative under statistical and risk neutral two-state VG Markov dynamics. These are employed in Section 5 to assess the improvements made by the two-state VG Markov model in both the statistical and risk neutral dimensions. All proofs are in the appendix.

## 1. The Structure of Lévy Processes

From a financial perspective the Lévy processes of interest to us are best introduced by contrast with the Merton (1976) jump diffusion model familiar in the finance literature. Such a jump diffusion model for the risk neutral stock price $S(t)$ is typically described by the stochastic differential equation

$$
\begin{equation*}
d S(t)=\left(r-\mu_{J}\right) S(t) d t+\sigma S(t) d W(t)+S\left(t_{-}\right)(J-1) d q \tag{1}
\end{equation*}
$$

where $r$ is the continuously compounded interest rate, $\sigma$ is the volatility from the diffusion component, $W(t)$ is a standard Brownian motion, $\mu_{J}$ is the mean jump size, $q(t)$ is a Poisson Jump or counting process that counts all the jumps and $J$ is the percentage jump in the stock price in that after the jump the stock price is $S\left(t_{-}\right) J$. Typically one models $J= e^{x}$ and $p(x)$ is the supposed probability density for jump in the logarithm of the stock price. With this specification with a Poisson arrival rate of $\lambda$ jumps per unit time we have that $\mu_{J}=\lambda \int_{-\infty}^{\infty}\left(e^{x}-1\right) p(x) d x$.

We see in equation (1) that the small price movements are being accounted for by the diffusion term while the jump terms model the few large and rare moves. One may now rewrite equation (1) by introducing separate Poisson processes $q^{x}(t)$ that count jumps of size $x$ that occur at rate $\lambda p(x)$ by the following expression

$$
\begin{equation*}
d S(t)=r S(t) d t+\sigma S(t) d W(t)+S\left(t_{-}\right) \int_{-\infty}^{\infty}\left(e^{x}-1\right)\left(d q^{x}(t)-\lambda p(x) d t\right) d x \tag{2}
\end{equation*}
$$

where we integrate over all jump sizes the jump less its arrival rate to get a martingale difference or a zero expectation impact just like the diffusion martingale difference.

From equation (2) to a general Lévy representation is a small step. First we introduce the space time Dirac delta measure $m(d x, d t)=\delta_{d q^{x}(t)-1} d t d x$ and rewrite (2) as

$$
\begin{equation*}
d S(t)=r S(t) d t+\sigma S(t) d W(t)+S\left(t_{-}\right) \int_{-\infty}^{\infty}\left(e^{x}-1\right)(m(d x, d t)-\lambda p(x) d x d t) \tag{3}
\end{equation*}
$$

The measure $\lambda p(x) d x d t$ is then called the compensator of the jump measure $m(d x, d t)$.

For a jump diffusion we have that the integral of the jump compensator

$$
\int_{-\infty}^{\infty} \lambda p(x) d x=\lambda<\infty
$$

and hence, we have a finite number of jumps in each time interval. Furthermore, if $p(x)$ is normally distributed with some mean and variance then the jump sizes may be centered away from zero.

The Lévy processes that are typically used in the literature for financial asset price dynamics essentially synthesize the small and large behavior in a unified way. First note that Brownian motion is a process of infinite variation and so has infinitely many price moves. Of course these moves are arbitrarily small in size to keep the process from blowing up. In a Lévy process we model the arrival rate of jumps of size of $x$ by a positive function $k(x)$ but allow for infinitely many jumps when the integral of the jump compensator

$$
\int_{-\infty}^{\infty} k(x) d x=-\infty
$$

This condition states that the aggregate arrival rate of jumps is infinite. However, for any specific size $a$ we must have that

$$
\int_{|x|>a} k(x) d x<\infty
$$

As a consequence the arrival rate goes to infinity near zero and the outcomes near zero are the most likely outcomes. Furthermore, one builds in the hypothesis that large moves are rarer than small ones by requiring $k(x)$ to be decreasing for $x>0$ and increasing for $x<0$.

Once we adopt an infinite activity Lévy process, it is shown in Carr, Geman, Madan and Yor (2000) that one may dispense with the diffusion component altogether as the small movements have now been synthesized into the jump component. The price process may now be compared with a continuum branching tree with a branch for each jump size and we have lost completeness. But this property was already lost in the introduction of the jump component in the jump diffusion models and does not constitute any additional complication. Risk neutral measures are often identified by inference from liquid markets in options.

Critical to the study of option prices and the statistical dynamics is the characteristic function for the logarithm of the stock price that characterizes the density of returns at all horizons. Carr and Madan (1999) demonstrate how effectively one may employ the fast Fourier transform to estimate option prices from this characteristic function. Maximum likelihood estimation is also made feasible by similar methods. Hence we focus considerable attention on the derivation of the characteristic function.

Apart from the Brownian motion in equation (3) we have the pure jump process

$$
X(t)=\int_{0}^{t} \int_{-\infty}^{\infty} x m(d x, d s)
$$

and for a Lévy density $k(x)$ its characteristic function reflects the homogeneous and independent increments and is given by

$$
E\left[e^{i u X(t)}\right]=\exp \left(t \int_{-\infty}^{\infty}\left(e^{i u x}-1\right) k(x) d x\right)
$$

The linearity in $t$ of the log characteristic function is a consequence of homogeneous and independent increments and we observe in the next section that this property has implications for the term structure of moments that are not in accord with the risk neutral data.

By way of an example of a pure jump Lévy process we mention the gamma process $\gamma(t ; v)$ with mean $t$ and variance $v t$. The process is an increasing process with increments over nonoverlaping intervals of length $h$ that have the gamma density with mean $h$ and variance vh. As a Lévy process its jump compensator is defined by

$$
k(x)= \begin{cases}\frac{\exp \left(-\frac{x}{\nu}\right)}{\nu x} & \mathrm{x}>0  \tag{4}\\ 0 & \mathrm{x}<0\end{cases}
$$

The integral of the jump compensator is infinite. We may easily evaluate its characteristic function and this is given by

$$
\phi_{\gamma(t ; \nu)}(u)=\left(\frac{1}{1-i u \nu}\right)^{t / \nu}
$$

Lévy processes arise naturally in the study of option prices from two perspectives. First from an empirical standpoint the presence of excess kurtosis in statistical return distributions and the presence of smiles in short maturity option implied volatilities both suggest that statistical and risk neutral local motions are not Gaussian with densities that are long-tailed to the normal. Lévy processes display various level of excess kurtosis and calibrate short maturity option prices remarkably well.

From a theoretical standpoint it is argued in Ané and Geman (2000) that normality of returns may be induced in an economic measure time obtained on counting the passage of economic time by counting for example the arrival of transactions, or some other measure of economic activity. Geman, Madan and Yor (2001) further analyze this situation and show that all time changes with a martingale component or what they call local uncertainty, are purely discontinuous processes. Two classic examples are the Normal Inverse Gaussian model introduced by Barndorff-Nielsen (1998) and the variance gamma model introduced by Madan and Seneta (1990). Both models are examples of Lévy processes.

## 2. Lévy Process Moment Term Structures

We recognize that Lévy processes work very well in explaining option prices at a single maturity and refer the reader to Madan, Carr and Chang (1998) and Carr, Madan,

Geman and Yor (2000) for empirical studies addressing this performance. The estimations are conducted separately for each maturity and we now seek to extend this quality of performance simultaneously across strike and maturity.

We are aware that the Lévy process models when forced to use a uniform set of parameters across multiple maturities fail to measure up to the task. We also comment that this has little to do with out-of-sample performance as that is a relevant issue for models whose in-sample performance is acceptable and the time evolution of the static parameters evolution has been modeled. At this juncture we seek acceptable in-sample performance at a single point in calendar time. What does this mean? What are the yardsticks for adequacy in in-sample performance?

One would like to have all pricing errors well within the bid-ask spreads for in-sample adequacy. ${ }^{1}$ We find that when the average percentage errors begin to exceed $10 \%$ that too many pricing errors are outside the bid-ask bounds. Hence, we generally use as a rule of thumb a $10 \%$ cutoff for the average percentage error. In that, if a model does not measure up to this yardstick then it is not a serious candidate for the representation of the information content of option prices, notwithstanding the statistical significance of its parameters and its domination on likelihood criteria of prior models.

At the other extreme we recognize that our in-sample yardsticks can be trivially met by infinite parameter structures that parameterize all the potential errors. We wish to attain dimensional reduction in synthesizing the information content of option prices at a single point in time for a single underlying by parsimoniously (in parameters) providing pricing performance well within the market spread. Success here is not guaranteed and we now address the issue that homogeneous Lévy processes are doomed to failure across the maturity spectrum.

We ask whether a mere generalization of the Lévy density of a homogeneous process of independent increments will suffice for modeling the risk neutral process of financial asset returns, especially as it pertains to variations across maturity. This is answered in the negative by first developing the theoretical moment term structures and comparing these with data on S\&P 500 Index options for 1999.

We first demonstrate that for all homogeneous Lévy processes volatility per unit time is constant with respect to the length of the time interval over which one observes the return. Furthermore, we note that skewness is inversely related to the square root of the length of the holding period while excess kurtosis is inversely related to the length of this period. This is a consequence of the linearity of the log characteristic function in the holding period. This pattern is then compared with the structure of this relationship as revealed in estimates of the term structure of these moments for the risk neutral process on the S\&P 500 Index over the year 1999.

## Proposition 1 Let $X(t)$ be a homogeneous Lévy process, then the Variance of $X(t)$ scales

with $t$, while skewness scales like $1=\sqrt{t}$ and excess kurtosis or kurtosis-3 scales like $1 / t$.

The appendix provides a proof. Here we describe the intuition behind the result by considering the calculation for the sum of two independent random variables $x_{1}, x_{2}$ with zero mean and identical but independent distributions. We wish to observe variance per
unit time as constant while skewness falls by a factor of $\sqrt{2}$ and excess kurtosis falls by $1 / 2$. Denote the sum by $x_{0}$ and the centered moments of order $k$, for $k=2,3,4$, by $m_{i}^{(k)}$, for $i=0,1,2$. Note that $m_{i}^{(1)}=0$. Let the common moments be $m^{(k)}$ without a subscript. Computing the moments we have

$$
\begin{aligned}
m_{0}^{(2)} & =m_{1}^{(2)}+m_{2}^{(2)}=2 m^{(2)} \\
m_{0}^{(3)} & =m_{1}^{(3)}+m_{2}^{(3)}=2 m^{(3)} \\
m_{0}^{(4)} & =m_{1}^{(4)}+6 m_{1}^{(2)} m_{2}^{(2)}+m_{2}^{(4)} \\
& =2 m^{(4)}+6\left[m^{(2)}\right]^{2} .
\end{aligned}
$$

Volatility per unit time is $m_{0}^{(2)} / 2=m^{(2)}$ and is constant. Skewness is

$$
\begin{aligned}
\frac{m_{0}^{(3)}}{\left[m_{0}^{(2)}\right]^{3 / 2}} & =\frac{2 m^{(3)}}{\left[2 m^{(2)}\right]^{3 / 2}} \\
& =\frac{1}{\sqrt{2}} \frac{m^{(3)}}{\left[m^{(2)}\right]^{3 / 2}}
\end{aligned}
$$

Finally, excess kurtosis is

$$
\begin{aligned}
\frac{m_{0}^{(4)}}{\left[m_{0}^{(2)}\right]^{2}}-3 & =\frac{2 m^{(4)}+6\left[m^{(2)}\right]^{2}}{4\left[m^{(2)}\right]^{2}}-3 \\
& =\frac{1}{2}\left(\frac{m^{(4)}}{\left[m^{(2)}\right]^{2}}-3\right) .
\end{aligned}
$$

Consider next the empirical term structure of risk neutral volatility, skewness and kurtosis as estimated on the S\&P 500 index daily for 1999. Figures 1, 2, and 3 present the estimated average term structures for each of the four quarters of 1999. The risk neutral moments for each maturity for each day are reverse engineered from the fit of the variance gamma model to the specific maturity on S\&P 500 index options for the day. The fits were conducted for each trading day of the year 1999. Seven maturities were taken ranging from one month to two years. The result was seven matrices with the number of rows equal to the number of trading days and four columns containing the maturity, the risk neutral volatility, skewness and kurtosis estimates for the particular maturity. The volatility is standardized to be per unit time while the skewness and kurtosis is for the particular maturity as constructed in Proposition 1. The seven matrices were then partitioned into four submatrices, one each for each quarter. What is plotted in Figures 1, 2, and 3 is the value of the quarterly average of the particular risk neutral

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-10.jpg?height=807&width=992&top_left_y=533&top_left_x=502)
Figure 1. Term structure of risk neutral volatility. The curves Q1, Q2, Q3, Q4 graph the average annualized volatility of the risk neutral distribution on S\&P 500 index options for the year 1999 against the average maturity. The averages are taken across daily estimates in the four quarters of the year.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-10.jpg?height=797&width=978&top_left_y=1462&top_left_x=513)
Figure 2. Term structure of risk neutral negative skewness. The curves Q1, Q2, Q3, Q4 graph the average skewness of the risk neutral distribution on S\&P 500 index options for the year 1999 against the average maturity. The averages are taken across daily estimates in the four quarters of the year.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-11.jpg?height=792&width=960&top_left_y=553&top_left_x=542)
Figure 3. Term structure of risk neutral excess kurtosis. The curves Q1, Q2, Q3, Q4 graph the average kurtosis of the risk neutral distribution on S\&P 500 index options for the year 1999 against the average maturity.The averages are taken across daily estimates in the four quarters of the year.

moment against the average maturity. The four curves in each figure refer to the four quarters.

We observe that volatility is not constant but rises somewhat with time to expiration, skewness does not decrease like the square root of the holding period, but in fact it rises, and excess kurtosis also increases instead of falling like the length of the holding period. This evidence in conjunction with proposition 1 strongly argues that a homogeneous Lévy process is not appropriate for describing the risk neutral dynamics of asset prices across the term structure of maturities.

## 3. Interarrival Times and the Mixture of Two Exponentials

A well known property of homogeneous Lévy processes is the fact that for such processes, interarrival times of jumps of a given size are exponentially distributed. To broadly assess this property we employed data on daily returns for 100 years on the Dow Jones Industrial Average. Here jumps are approximated by the daily move. First the interarrival times of moves between $2 \%$ and $3 \%, 3 \%$ and $4 \%$, and $4 \%$ and $5 \%$, independent of sign are obtained. Denote these size intervals for moves by $u=1,2,3$.

For each of the three move size intervals we count the number of days between moves with sizes in this interval and then construct a histogram of the resulting interarrival times by sorting the day counts into 50 bins of equal sizes of 16,40 and 50 days per bin for the

Table 1. Results of Goodness of Fit Tests on Interarrival Times Between Daily Return Movements of Specific Sizes on the Dow Jones Industrial Average
| Size of Move | Exponential Distribution |  | Two Exponentials |  |
| :--- | :--- | :--- | :--- | :--- |
|  | $Q_{n}^{*}$ | $\chi_{k-s-1}^{2}$ | $Q_{n}^{*}$ | $\chi_{k-s-1}^{2}$ |
| 2-3\% | 1668.21* | 65.17 | 61.14 | 62.83 |
| 3-4\% | 825.52* | 65.17 | 55.22 | 62.83 |
| 4-5\% | 412.64* | 65.17 | 52.78 | 62.83 |


Note: Presented are chi-squared statistics for the interarrival histogram for the number of days between the log price relative movements in three size classes for two estimated models for this density. Significance is at the five percent level. The exponential law and a mixture of two exponentials provide the theoretical arrival rates in the bins of the histogram.
three size intervals, respectively. Let $I_{j}$ denote the time interval for the $j$ th bin. We next obtained count statistics $z_{j}^{u}$ for $j=1, \ldots, 50$ of the number of times for size $u$ the interarrival time for a jump of this size was an element of $I_{j}$.

To explain these interarrival time distributions two candidate models are investigated, first is an exponential distribution implied by any homogeneous Lévy process with density $p_{1}(t)=\theta e^{-\theta \tau}$ with mean interarrival time $1 / \theta$ and second we use a mixture of two exponentials with density $p_{2}(t)=\pi \theta_{1} e^{-\theta_{1} t}+(1-\pi) \theta_{2} e^{-\theta_{2} t}$. For an interarrival time density $p(t ; \Theta)$ the probability of an arrival in the bin $I_{j}$ is given by

$$
p_{j}(\Theta)=\int_{I_{j}} p(t, \Theta) d t
$$

and the chi-squared statistic for $n$ data items is defined by

$$
Q_{n}(\Theta)=\sum_{j=1}^{k}\left(\frac{\left(z_{j}^{u}-n p_{j}(\Theta)\right)^{2}}{n p_{j}(\Theta)}\right) .
$$

In each case we obtained the minimum chi-squared statistic

$$
Q_{n}^{*}=\min _{\Theta} Q_{n}(\Theta)
$$

and report in Table 1 below the $5 \%$ critical value of this statistic $\chi_{k-s-1}^{2}$ where $s$ is the number of parameters estimated, along with $Q_{n}^{*}$.

Observe from Table 1 the strong rejection of the exponential model and equally interestingly the acceptance of the model that mixes just two exponential densities. This contrast in the performance of these two interarrival time models is more clearly evident from Figures 4, 5, and 6 that display the fitted and empirical cumulative distribution functions. In the graphs below, the $x$-axis is the interarrival time in days and the $y$-axis is the corresponding value of respectively empirical (solid line), exponential (--) and mixture

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-13.jpg?height=695&width=861&top_left_y=542&top_left_x=616)
Figure 4. Cumulative distribution function of data on interarrival times for the daily log price relative of the Dow Jones Industrial average. The figure shows the cumulative distribution function for interarrival times of daily absolute returns between 2 and 3 percent. Also presented is the best fit by the exponential model and the mixture of two exponentials. The horizontal axis measures interarrival times in days while the vertical axis is the cumulative probability. The lower graph presents the absolute value of the difference between the fitted and empirical cumulative distribution functions.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-13.jpg?height=675&width=843&top_left_y=1487&top_left_x=628)
Figure 5. Cumulative distribution function of data on interarrival times for the daily log price relative of the Dow Jones Industrial average. The figure shows the cumulative distribution function for interarrival times of daily absolute returns between 3 and 4 percent. Also presented is the best fit by the exponential model and the mixture of two exponentials. The horizontal axis measures interarrival times in days while the vertical axis is the cumulative probability. The lower graph presents the absolute value of the difference between the fitted and empirical cumulative distribution functions.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-14.jpg?height=661&width=815&top_left_y=542&top_left_x=628)
Figure 6. Cumulative distribution function of data on interarrival times for the daily log price relative of the Dow Jones Industrial average. The figure shows the cumulative distribution function for interarrival times of daily absolute returns between 4 and 5 percent. Also presented is the best fit by the exponential model and the mixture of two exponentials. The horizontal axis measures interarrival times in days while the vertical axis is the cumulative probability. The lower graph presents the absolute value of the difference between the fitted and empirical cumulative distribution functions.

of two exponentials (- .) cumulative distribution function. Right under these graphs, there are graphs of the absolute value of the difference between the fitted cumulative distribution functions and the empirical one.

These observations are suggestive of the possibility of combining just two homogeneous Lévy processes and postulating that the dynamics shifts randomly between these two homogeneous Lévy states. Each homogeneous Lévy process has exponential interarrival times and the fact that a mixture of two exponentials characterizes interarrival times could result from a statistical dynamics that moves between these homogeneous process states. The relevance of such a representation for the risk neutral process then follows by equivalence. The rejection of an exponential interarrival time however, does argue against the relevance of any homogeneous Lévy process as appropriate for describing the statistical dynamics.

## 4. The Two-State VG Markov Model

The variance gamma model is first summarized along with the role played by each of its parameters. This is followed by the definition of the two-state variance gamma Markov model and a discussion of its properties. Next we develop the characteristic function for the two-state variance gamma Markov model.

### 4.1. The Variance Gamma Model

The VG process is a three parameter process $X(t ; \sigma, \nu, \theta)$ obtained on time changing Brownian with drift, $\theta t+\sigma W(t)$, for a standard Brownian motion $W(t)$, by an independent gamma process $\gamma(t ; \nu)$ with unit mean rate and variance rate $\nu$. The parameter $\theta$ provides control over skewness while $\nu$ measures the percentage excess kurtosis over 3, the kurtosis of the normal distribution, in the special case of $\theta=0$. The process is a finite variation process and can be written as the difference of two increasing processes that in this case are both gamma processes. For these details the reader is referred to Madan, Carr and Chang (1998) or Carr, Geman, Madan and Yor (2000).

The characteristic function of the VG process has a particularly simple expression and is given by

$$
\begin{equation*}
\Phi_{X(t)}(u)=E\left[e^{i u X(t)}\right]=\left(1-i \theta \nu u+\frac{\sigma^{2} \nu}{2} u^{2}\right)^{-t / \nu} . \tag{5}
\end{equation*}
$$

We may observe on taking the limit as $\nu$ tends to zero that the characteristic function tends to $\exp \left(-\sigma^{2} u^{2} t / 2\right)$ the characteristic of the normal distribution and hence that standard Brownian motion is a parametric special case. Processes obtained by subordinating Brownian motion to a time change have Brownian motion as the special case arising when the volatility of the time change approaches zero.

Unlike Brownian motion however, the process is a pure jump process that is infinitely divisible with independent increments and has a Lévy density that may be recovered from the Lévy Khintchine characterization of the characteristic function for such processes. This Lévy density is given by

$$
\begin{align*}
k(x) & =\frac{1}{\nu|x|} \exp \left(-\left(\zeta x+\frac{\sqrt{2}}{s \sqrt{\nu}}|x|\right)\right) \\
\zeta & =-\frac{\theta}{\sigma^{2}} \\
s & =\frac{\sigma}{\sqrt{1+\left(\frac{\theta}{\sigma}\right)^{2} \frac{\nu}{2}}} \tag{6}
\end{align*}
$$

We comment that the infinite activity may be observed on noting the division by $|x|$ in the Lévy density and hence we get that the aggregate arrival rate or integral of the Lévy density is infinite. The fact that we have a difference of two gamma processes may also be seen by comparing (6) for positive and negative $x$ values with the gamma Lévy density encountered earlier in equation (4). Note also that $\theta=0$ produces a symmetric Lévy density while negative values for $\theta$ raise the arrival rate of negative jumps relative to positive jumps thereby building a left skew. Finally increasing $\nu$ lowers the rate of exponential decay of the Lévy density symmetrically on both sides and this raises the arrival rates of jumps across all sizes and builds kurtosis. For the symmetric case the kurtosis is precisely $3(1+\nu)$, whereby $\nu$ calibrates the percentage excess kurtosis.

The VG stockprice process is given by

$$
\begin{equation*}
S(t)=S(0) \exp (\mu t+X(t)+\omega t) \tag{7}
\end{equation*}
$$

where $\mu$ is the mean rate of return on the stock that for risk neutral processes equals the interest rate, and $\omega$ is the convexity correction defined by

$$
\begin{equation*}
E\left[e^{X(t)}\right]=\Phi_{X(t)}(-i)=e^{-\omega t} \tag{8}
\end{equation*}
$$

Specifically we have that

$$
\begin{equation*}
\omega=-\frac{1}{t} \log \left(\Phi_{X(t)}(-i)\right)=\frac{1}{\nu} \log \left(1-\theta \nu-\frac{\sigma^{2} \nu}{2}\right) \tag{9}
\end{equation*}
$$

Option prices and densities may be estimated using the methods described in Carr, Geman, Madan and Yor (2000), Carr and Madan (1999), or the closed forms derived in Madan, Carr and Chang (1998).

### 4.2. The Two-State Variance Gamma Markov Model

The two state VG Markov model is driven by two VG processes $X_{i}\left(t ; \sigma_{i}, \nu_{i}, \theta_{i}\right)$ for $i \in \{0,1\}$ and a two-state Markov chain $U(t)$ that takes values in the set $\{0,1\}$. Specifically, the dynamics of the two-state VG process $X(t)$ is given by

$$
\begin{equation*}
X(t)=\int_{0}^{t}(1-U(s)) d X_{0}(s)+U(s) d X_{1}(s) \tag{10}
\end{equation*}
$$

The price process for the two state VG Markov model is

$$
\begin{equation*}
S(t)=S(0) \exp (r t+\omega(t)+X(t)) \tag{11}
\end{equation*}
$$

where $\omega(t)$ is defined by the condition

$$
E\left[e^{X(t)}\right]=e^{-\omega(t)}
$$

The Markov chain $U(t)$ has state transition rates given by parameters $\lambda_{01}, \lambda_{10}$ for transition from 0,1 to 1,0 . Suppose that the initial state is 0 with probability $p$. The total number of parameters for the model is $9, \sigma_{0}, \nu_{0}, \theta_{0}, \sigma_{1}, \nu_{1}, \theta_{1}, \lambda_{01}, \lambda_{10}$ and $p$.

Some of the attractive features of this model are as follows. First, given the observation that options at different maturities are calibrated well by the variance gamma model, undoubtedly with different parameter sets, we expect that the two state variance gamma Markov model with its two variance gamma states would be capable of at least calibrating to an initial segment of the volatility surface. Second by altering the probability of the
initial state the model should be able to represent both rising or declining term structures of volatility in the option maturity direction. Third by virtue of adjusting the transition probabilities one should be able to capture a range of clustering characteristics in the underlying volatility process. Fourth, unlike continuous state mean reverting hidden volatility processes, as in the Heston (1993) construction, we have here a simple hidden state that just takes two values with the process potentially spending reasonable amounts of time in each state.

### 4.3. Closed Forms for the Characteristic Function

To construct the characteristic function of the two-state variance gamma Markov model, let $\phi_{i}(u)$ denote the characteristic functions for the two embedded variance gamma processes. If in $t$ units of time the time spent by the process $U(t)$ in state 1 is $s$, for $0 \leq s \leq t$, then by the independence of the two variance gamma processes and the resulting multiplicativity of the characteristic functions involved we have that

$$
\begin{equation*}
\phi_{X}(u)=\int_{0}^{t} \phi_{0}(u)^{t-s} \phi_{1}(u)^{s} f(s) d s \tag{12}
\end{equation*}
$$

where $f(s)$ is the density of the time spent in state 1 . We may rewrite (12) in terms of the Laplace transform of the density for the time spent in state 1 . In particular we may write,

$$
\phi_{X}(u)=\phi_{0}(u)^{t} \int_{0}^{t} \exp \left(-s \log \left(\frac{\phi_{0}(u)}{\phi_{1}(u)}\right)\right) f(s) d s
$$

Defining the Laplace transform of the density $f$ by

$$
\begin{equation*}
g(\lambda)=\int_{0}^{t} e^{-\lambda s} f(s) d s \tag{13}
\end{equation*}
$$

and note that

$$
\phi_{X}(u)=\phi_{0}(u)^{t} g\left(\log \left(\frac{\phi_{0}(u)}{\phi_{1}(u)}\right)\right) .
$$

The analysis to this point can be easily repeated for any two other Lévy processes replacing the role of the variance gamma processes in the development. Observe that the resulting characteristic function is analytic in the Laplace Transform of the time spent in state 1 of a two state Markov chain. We now determine this Laplace transform. ${ }^{2}$

Define by $Z(t)$ the vector process $(U(t), Y(t))$ where

$$
Y(t)=\int_{0}^{t} U(s) d s
$$

is the time spent in state 1 . The vector process $Z$ is Markov and so the conditional expectation of the exponential of $(a U(t)+b Y(t))$ has the structure

$$
E\left[e^{a U(t)+b Y(t)} \mid \Im_{s}\right]=f(s, U(s), Y(s))
$$

The function $f$ has the exponential affine form

$$
f(s, U(s), Y(s))=\exp (\alpha(s)+\beta(s) Y(s)+\gamma(s) U(s))
$$

and it remains to determine the coefficient functions $((\alpha(s), \beta(s), \gamma(s)), 0 \leq s \leq t)$ with boundary conditions $\alpha(t)=\gamma(t)=0$ and $\beta(t)=-\lambda$.

Suppose that the transition rates for the process $U$ are $\lambda_{01}, \lambda_{10}$ from states 0 to 1 and vice versa. Hence the expectation of $d U$ is $\lambda_{01} d t$ when $U(t)=0$ and it is $-\lambda_{10} d t$ when $U(t)=1$.

The martingale condition for the function $f$ yields the condition

$$
\begin{aligned}
0= & f\left(\alpha^{\prime}+\beta^{\prime} Y+\gamma^{\prime} U+\beta U+\gamma\left(\lambda_{01}(1-U)-\lambda_{10} U\right)\right) \\
& +\lambda_{01}(1-U) f\left(e^{\gamma}-1-\gamma\right) \\
& +\lambda_{10} U f\left(e^{-\gamma}-1+\gamma\right)
\end{aligned}
$$

Since this must hold for all values of $Y, U$ we have three differential equations

$$
\begin{aligned}
\beta^{\prime} & =0 \\
\gamma^{\prime}+\beta-\lambda_{01}\left(e^{\gamma}-1\right)+\lambda_{10}\left(e^{-\gamma}-1\right) & =0 \\
\alpha^{\prime}+\lambda_{01}\left(e^{\gamma}-1\right) & =0
\end{aligned}
$$

It follows from the boundary conditions that $\beta(t)=-\lambda$. Multiplying the second equation by $e^{\gamma}$ and letting $\psi=e^{\gamma}$ we have the equations

$$
\begin{aligned}
\psi^{\prime}+\left(\lambda_{01}-\lambda_{10}-\lambda\right) \psi-\lambda_{01} \psi^{2}+\lambda_{10} & =0 \\
\alpha^{\prime}+\lambda_{01}(\psi-1) & =0
\end{aligned}
$$

The Laplace transforms conditional on starting in state 0 and 1 respectively are

$$
\begin{aligned}
& g_{0}(\lambda)=\exp (\alpha(0)) \\
& g_{1}(\lambda)=\exp (\alpha(0)) \psi(0)
\end{aligned}
$$

and if the initial probability of state 0 is $p$ then

$$
g(\lambda)=p g_{0}(\lambda)+(1-p) g_{1}(\lambda) .
$$

The equation for $\psi$ is the well known Ricatti equation and has a solution given by

$$
\psi(s)=\frac{1}{\lambda_{01}} \frac{\eta_{2}\left(\eta_{1}+\lambda_{01}\right) e^{-\left(\eta_{2}-\eta_{1}\right)(t-s)}-\eta_{1}\left(\eta_{2}+\lambda_{01}\right)}{\eta_{2}+\lambda_{01}-\left(\eta_{1}+\lambda_{01}\right) e^{-\left(\eta_{2}-\eta_{1}\right)(t-s)}}
$$

where

$$
\eta_{1}, \eta_{2}=\frac{\lambda+\lambda_{10}-\lambda_{01}}{2} \pm \sqrt{\frac{\left(\lambda+\lambda_{10}-\lambda_{01}\right)^{2}}{4}+\lambda_{10} \lambda_{01}}
$$

The value for $\alpha(0)$ is obtained on integration

$$
\begin{aligned}
\alpha(0) & =-\int_{0}^{t} \alpha^{\prime}(s) d s \\
& =\lambda_{01} \int_{0}^{t}(\psi(s)-1) d s
\end{aligned}
$$

An explicit integration of $\psi$ yields that

$$
\begin{aligned}
& g_{0}(\lambda)=\exp (\alpha(0))=\exp \left(-\left(\eta_{1}+\lambda_{01}\right) t\right) \frac{\eta_{2}+\lambda_{01}-\left(\eta_{1}+\lambda_{01}\right) e^{-\left(\eta_{2}-\eta_{1}\right) t}}{\eta_{2}-\eta_{1}} \\
& g_{1}(\lambda)=\frac{1}{\lambda_{01}} \exp \left(-\left(\eta_{1}+\lambda_{01}\right) t\right) \frac{\eta_{2}\left(\eta_{1}+\lambda_{01}\right) e^{-\left(\eta_{2}-\eta_{1}\right) t}-\eta_{1}\left(\eta_{2}+\lambda_{01}\right)}{\eta_{2}-\eta_{1}}
\end{aligned}
$$

In summary, we have the result of the following proposition.

Proposition 2 For the two-state VG Markov price process of equation (11) the characteristic function of the log price is given in terms of nine parameters, $\sigma_{0}, \nu_{0}, \theta_{0}, \sigma_{1}$, $\nu_{1}, \theta_{1}, p, \lambda_{01}, \lambda_{10} b y$

$$
\begin{aligned}
\phi_{\ln S(t)}(u) & =\exp (i u(\ln (S(0)))+(r t+\omega(t))) \phi_{X(t)}(u) \\
\phi_{X(t)}(u) & =\phi_{0}(u)^{t} g\left(\log \left(\frac{\phi_{0}(u)}{\phi_{1}(u)}\right)\right) \\
g(\lambda) & =p g_{0}(\lambda)+(1-p) g_{1}(\lambda) \\
\phi_{0}(u) & =\left(1-i \theta_{0} \nu_{0} u+\frac{\sigma_{0}^{2} \nu_{0}}{2} u^{2}\right)^{-1 / \nu_{0}} \\
\phi_{1}(u) & =\left(1-i \theta_{1} \nu_{1} u+\frac{\sigma_{1}^{2} \nu_{1}}{2} u^{2}\right)^{-1 / \nu_{1}} \\
g_{0}(\lambda) & =\exp \left(-\left(\eta_{1}(\lambda)+\lambda_{01}\right) t\right) \frac{\eta_{2}(\lambda)+\lambda_{01}-\left(\eta_{1}(\lambda)+\lambda_{01}\right) e^{-\left(\eta_{2}(\lambda)-\eta_{1}(\lambda)\right) t}}{\eta_{2}(\lambda)-\eta_{1}(\lambda)} \\
g_{1}(\lambda) & =\frac{1}{\lambda_{01}} \exp \left(-\left(\eta_{1}(\lambda)+\lambda_{01}\right) t\right)
\end{aligned}
$$

$$
\begin{aligned}
& \times \frac{\eta_{2}(\lambda)\left(\eta_{1}(\lambda)+\lambda_{01}\right) e^{-\left(\eta_{2}(\lambda)-\eta_{1}(\lambda)\right) t}-\eta_{1}(\lambda)\left(\eta_{2}(\lambda)\left(\eta_{2}(\lambda)+\lambda_{01}\right)\right.}{\eta_{2}(\lambda)-\eta_{1}(\lambda)} \\
\eta_{1}(\lambda), \eta_{2}(\lambda)= & \frac{\lambda+\lambda_{10}-\lambda_{01}}{2} \pm \sqrt{\frac{\left(\lambda+\lambda_{10}-\lambda_{01}\right)^{2}}{4}+\lambda_{10} \lambda_{01}} \\
\omega(t)= & -\ln \left(\phi_{X(t)}(-i)\right)
\end{aligned}
$$

We observe from the nonlinearity of $\log$ characteristic function of $X(t)$ in $t$ as may be observed from the expressions for $g_{0}, g_{1}$ that the process for $X(t)$ is not a Lévy process and does not therefore suffer the negative features outlined in Proposition 1. Second we note that the stock price process defined by equation (11) is a process of unit discounted expectation by construction and pricing excludes static arbitrages and calendar spread arbitrages. The process is however not a martingale as the mean correction does not typically induce zero conditional expectations for the price motion when the underlying process, in this case, $X(t)$ is not one of independent increments. For a further discussion of these issues the reader is referred to Carr, Geman, Madan and Yor (2001) where a similar construction to the one adopted here is seen to dominate in pricing.

## 5. Data and Estimation Methodology

To assess the empirical adequacy of this two-state VG Markov model as a candidate for both the statistical and risk neutral process for the prices of financial assets, we obtained time series data on daily returns for 22 underlying assets and data on option prices for six of these assets on five Wednesdays. The time series data was for the period January 3, 1994 to December 28, 1998 while the options data was for October 14, 1998, November 11, 1998, December 9, 1998, January 13, 1999 and February 10, 1999. Though more extensive estimations may easily be conducted, our purpose is to assess the adequacy of the option pricing model for in-sample representation of the information content of option prices at a single point in calendar time. Essentially if the model begins to meet adequacy standards for all of 30 cases using a variation of names and dates then the model is a candidate for the more extensive task of implementing it daily for a large class of underliers.

For the time series data we employ a modification of the method of maximum likelihood estimation. Direct maximum likelihood estimation would require an inversion of the characteristic function at each of 1260 data points to evaluate the likelihood function and this is computationally expensive, noting that these inversions must then be made at a variety of parameter points called by an optimization algorithm. Instead of evaluating the likelihood of the raw data, we binned our data into a prespecified set of centered points that coincide with the points at which a Fast Fourier inversion evaluates the density, and then a single application of the Fast Fourier transform yields the likelihood of the binned data. The statistical parameters are estimated by maximizing the likelihood of this binned data.

The risk neutral process is fit by matching model prices to market prices using nonlinear least squares. To obtain the option price from the characteristic function we follow

Carr and Madan (1999) and invert the Fourier transform in log strike, of the time value of the option. Carr and Madan (1999) relate this Fourier transform analytically to the characteristic function of the logarithm of the stock price at maturity. Specifically evaluating the time value of an option of maturity $T$, with strike $K=e^{k}$ as $z_{T}(k)$ equal to the value of a put option for strikes below the current forward price and the value of a call option when $K$ exceeds the forward, its Fourier transform is

$$
\begin{equation*}
\zeta_{T}(v)=\int_{-\infty}^{\infty} e^{i v k} z_{T}(k) d k \tag{14}
\end{equation*}
$$

One may explicitly relate $\zeta_{T}(v)$ of equation (14) to the characteristic function of the log of the stock price, $\phi_{\ln (S(T))}(u)$, given in Proposition 2. For completeness we present here a slight generalization that accommodates an arbitrary forward price.

Proposition 3 The Fourier transform of time value is analytically related to the log characteristic function by

$$
\zeta_{T}(v)=e^{-r T} \frac{F_{0}^{1+i v}-\phi_{\ln (S(T))}(v-i)}{v(v-i)}
$$

where $F_{0}$ is the current forward price given by $S(0) e^{(r-\delta) T}$ for a dividend yield of $\delta \%$ per year.

From Proposition 3, one may obtain call prices $C_{T}(K)$ and put prices $P_{T}(K)$ by Fourier inversion as

$$
\begin{align*}
& C_{T}(K)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-i v k} \zeta_{T}(v) d v+e^{-r T}\left(F_{0}-K\right)^{+}  \tag{15}\\
& P_{T}(K)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-i v k} \zeta_{T}(v) d v+e^{-r T}\left(K-F_{0}\right)^{+} \tag{16}
\end{align*}
$$

The integrations in equations (15) and (16) may be performed using the fast Fourier transform incorporating Simpson's s rule.

Specifically, let $v_{j}=-a+(j-1) \eta$, for $j=1, \ldots, N$, where $N$ is a power of 2 and $\eta=2 a / N$. Further, let $k_{u}=-b+(u-1) \lambda$ for $u=1, \ldots, N$, where $\lambda=2 b / N$. For the use of the Fast Fourier transform we require that $\lambda \eta=2 / N$. Incorporating Simpson's rule we may write the integration in (15) and (16) as

$$
\begin{aligned}
\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-i v k_{u}} \zeta_{T}(v) d v & \approx \frac{1}{2 \pi} \sum_{j=1}^{N} e^{-i v_{j} k_{u}} \zeta_{T}\left(v_{j}\right) \frac{\eta}{3}\left(3+(-1)^{j}-\delta_{j-1}\right) \\
& =\frac{1}{2 \pi} \sum_{j=1}^{N} e^{-i(-a+(j-1) \eta)(-b+(u-1) \lambda)} \zeta_{T}\left(v_{j}\right) \frac{\eta}{3}\left(3+(-1)^{j}-\delta_{j-1}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{e^{i a k_{u}}}{2 \pi} \sum_{j=1}^{N} e^{-i(j-1)(u-1) \lambda \eta} \zeta_{T}\left(v_{j}\right) e^{i b \eta(j-1)} \frac{\eta}{3}\left(3+(-1)^{j}-\delta_{j-1}\right) \\
& =\frac{e^{i a k_{u}}}{2 \pi} \sum_{j=1}^{N} e^{-i(2 \pi / N)(j-1)(u-1)} \zeta_{T}\left(v_{j}\right) e^{i b \eta(j-1)} \frac{\eta}{3}\left(3+(-1)^{j}-\delta_{j-1}\right) \\
& =\frac{e^{i a k_{u}}}{2 \pi} f f t\left\{\zeta_{T}\left(v_{j}\right) e^{i b \eta(j-1)} \frac{\eta}{3}\left(3+(-1)^{j}-\delta_{j-1}\right)\right\}
\end{aligned}
$$

where $f f t$ denotes the application of the Fast Fourier transform operator.
These operations make it possible to obtain two-state VG Markov option prices at a sufficiently high speed to make calibration of parameters to the options surface a feasible exercise. In our applications we calibrated by minimizing the sum of squared relative errors and report the average percentage error as the statistic of best fit.

## 6. Time Series Results

For the 22 underlying asset prices, we estimated the geometric Brownian motion model, the VG model and the two-state VG Markov model as the underlying dynamics for the daily log price relative. We report in Tables 2(a) and 2(b) the Black Scholes and VG parameter estimates, and in Tables 3(a) and 3(b) the two-state VG Markov parameter estimates. Tables 4(a) and 4(b) present the three likelihoods along with two likelihood ratio test statistics for VG relative to Black Scholes and two-state MarkovVG relative toVG.

Comparing VG and Black Scholes briefly, we observe that the VG parameters are significant and the estimate for $\sigma$ is generally in line with the Black Scholes or statistical volatility, though somewhat smaller in most cases. The parameters $\nu$ and $\theta$ typically correct for the tail behavior of the density. The Black Scholes model is rejected in favor of the VG in all cases by the likelihood ratio test statistic, a finding that is consistent with earlier results on the VG reported in Madan, Carr and Chang (1998).

For the comparison of VG and two-state VG Markov, we note that the estimates of state transition rates are typically highly significant and this confirms the validity of at least a two state hypothesis. The likelihood ratio tests also reject VG in favor of the two-state VG Markov model. The precision of the higher order parameters is however diminished relative to the VG model. It is also interesting to observe that for many cases the estimate for the average time spent in a state, the reciprocal of the estimate for $\lambda_{01}, \lambda_{10}$ is of the order of four to six months for the single names like IBM, INTC, and JNJ. For the indices like SPX or RUT this average time spent in a state decreases to one month. Comparing the two states we observe that the state with the higher volatility, $\sigma$, also has the higher level of skewness and kurtosis and so one may think of the states as reflecting less or more risks of market movement. A glance at the column for state probability shows the pattern of a generally higher probability of being in the less risky state or the forecast of a potential move to a more risky state. This is evidence that one would expect to be consistent with

Table 2(a). Statistical Parameter Estimates for Single Names
| Ticker | GBM | VG |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | $\sigma$ | $\sigma$ | $\nu$ | $\theta$ |
| BA | . 2831 (1.04e-6) | . 2781 (.0187) | . 0024 (.0008) | -. 0109 (.0073) |
| GE | . 2378 (1.12e-9) | . 235 (.0012) | . 0014 (.0007) | . 1262 (.0027) |
| HWP | . 3681 (.001) | . 3573 (.0234) | . 0022 (.0008) | . 0944 (.2766) |
| IBM | . 3128 (1.13e-5) | . 3037 (.019) | . 0025 (.0008) | . 2185 (.1007) |
| INTC | . 3692 (4.3e-5) | . 3646 (.0269) | . 0013 (.0008) | . 2653 (.2127) |
| JNJ | . 238 (7.32e-6) | . 2376 (.0001) | . 0013 (.0007) | . 1016 (.0038) |
| MCD | . 2497 (9.24e-7) | . 2446 (.0049) | . 0019 (.0019) | . 0507 (.0206) |
| MMM | . 2333 (1.11e-9) | . 2316 (.0059) | . 0027 (.0008) | -. 091 (.0065) |
| MRK | . 2608 (5.19e-6) | . 2581 (.0057) | . 0014 (.0007) | . 1353 (.0173) |
| MSFT | . 3314 (1.25e-4) | . 3298 (.0174) | . 0012 (.0007) | . 3795 (.0575) |
| UAL | . 3595 (2.23e-4) | . 3588 (.022) | . 0014 (.0007) | . 0979 . 1509 |
| WMT | . 3064 (5.84e-6) | . 3028 (.025) | . 0015 (.0008) | . 0115 (.0037) |
| XON | . 2152 (7.56e-10) | . 2149 (3.87e-4) | . 0016 (1.85e-4) | . 0074 ( $1.075 \mathrm{e}-4$ ) |
| YHOO | . 5573 (.025) | . 5517 (.0427) | . 0042 (.001) | . 5434 (.4846) |


Note: Presented are maximum likelihood estimates of the geometric Brownian motion (GBM) model and the variance gamma (VG) model based on time series return data for a variety of stock price series. Standard errors are in parentheses. The data period is January 3, 1994 to December 9, 1998. Under the GBM model $x \log (S(t) / S(0))$ - mean $=\sigma Z$, where $Z$ is normally distributed with mean 0 and variance $t$. Under the VG model $\log (S(t) / S(0))$ - mean $=\theta(g-t)+\sigma Z$, where $Z$ is normally distributed with mean 0 and variance $g$ and $g$ is distributed as a gamma variate with mean $t$ and variance $\nu t$.
our earlier observation of increases in volatility, skewness and kurtosis as we increase the time to expiration.

These findings lead us to tentatively conclude that the model is capable of capturing some interesting dimensions of the underlying stochastic process, even from just observations on daily returns. To get a greater appreciation for the workings of these maximum likelihood estimation procedures we present graphs of the binned data and the fitted likelihood in three cases, BA, HWP and SPX. These are given in Figures 7, 8, and 9. They show the ability of the two-state VG Markov model to get closer to the pattern reflected in the data.

Table 2(b). Statistical Parameter Estimates for Market Indexes
| Ticker | GBM | VG |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | $\sigma$ | $\sigma$ | $\nu$ | $\theta$ |
| BIX | . 2149 (1.14e-9) | . 2119 (.0011) | . 0026 (.0008) | . 0708 (..027) |
| BKX | . 2203 (1.12e-9) | . 217 (.0007) | . 0026 (.0008) | . 0569 (.0012) |
| DRG | . 1888 (7.2e-10) | . 1857 (.0052) | . 0026 (.0008) | . 1313 (.0057) |
| RUT | . 1325 (4.73e-10) | . 1276 (.0085) | . 0038 (.0009) | . 0587 (.0354) |
| SOX | . 379 (8.24e-5) | . 3754 (.0226) | . 0014 (.0008) | . 0686 (.193) |
| SPX | . 1377 (3.94e-10) | . 1414 (.0106) | . 0034 (.0009) | . 0564 (.027) |
| XAU | . 3737 (1.29e-3) | . 3681 (.0219) | . 0018 (.0008) | -. 3343 (.0037) |
| XOI | . 1587 (7.06e-10) | . 1575 (.0048) | . 0022 (.0007) | . 004 (.0095) |


Note: Presented are maximum likelihood estimates of the geometric Brownian motion (GBM) model and the variance gamma (VG) model based on time series return data for a variety of stock price indices. Standard errors are in parentheses. The data period is January 3, 1994 to December 9, 1998. Under the GBM model $\log (S(t) / S(0))$ - mean $=\sigma Z$, where $Z$ is normally distributed with mean 0 and variance $t$. Under the VG model $\log (S(t) / S(0))$ - mean $=\theta(g-t)+\sigma Z$, where $Z$ is normally distributed with mean 0 and variance $g$ and $g$ is distributed as a gamma variate with mean $t$ and variance $\nu t$.

## 7. Risk Neutral Results

The risk neutral process was calibrated to market close option prices on 6 underliers for each of five Wednesdays for all strikes and the first three to five maturities. For each maturity we have between 10 to 20 strikes available at that maturity, depending on the name. The largest data set is for the SPX where we often have up to 20 strikes for each maturity. Tables 5(a) to 5(e) report the results of these estimations.

We observe a reasonable ability for the two-state VG Markov model to calibrate to all strikes for the first three maturities, and in some cases the performance may be extended to five maturities. For example, IBM options for maturities up to 2.269 years could be explained with a relative percentage error as little as $2.84 \%$ on October 14, 1998. More generally, five maturities were consistently within our cutoff for IBM and INTC. Moreover, for these two names we observe a consistent estimate of a high probability of being in the state with the higher risk neutral $\sigma$, and an anticipation that in about six months to a year, the state will be one of a lower $\sigma$.

For the SPX we have a considerable probability of being in a relatively high $\sigma$ state with typical VG parameter estimates (we note the estimates for October, November, December

Table 3(a). Statistical Estimates of the Two-State VG Markov Model for Single Names
| Parameters | BA | (se) | GE | (se) | HWP | (se) | IBM | (se) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\sigma_{0}$ | . 375 | 4.14e-2 | . 282 | 1.81e-3 | . 451 | $4.92 \mathrm{e}-2$ | . 259 | $1.62 \mathrm{e}-2$ |
| $\nu_{0}$ | $2.76 \mathrm{e}-3$ | $2.03 \mathrm{e}-3$ | $2.83 \mathrm{e}-3$ | $1.58 \mathrm{e}-3$ | $3.37 \mathrm{e}-3$ | $2.89 \mathrm{e}-3$ | $8.184 \mathrm{e}-4$ | $7.85 \mathrm{e}-4$ |
| $\theta_{0}$ | $3.24 \mathrm{e}-3$ | $5.68 \mathrm{e}-3$ | 1.1e-2 | $1.22 \mathrm{e}-2$ | . 464 | $9.53 \mathrm{e}-2$ | . 108 | . 195 |
| $\sigma_{1}$ | . 207 | $2.58 \mathrm{e}-3$ | . 204 | $9.59 \mathrm{e}-4$ | . 285 | $3.91 \mathrm{e}-2$ | . 795 | $6.62 \mathrm{e}-2$ |
| $\nu_{1}$ | $1.7 \mathrm{e}-3$ | $1.16 \mathrm{e}-3$ | $4.9 \mathrm{e}-5$ | $3.71 \mathrm{e}-4$ | $1.66 \mathrm{e}-4$ | $1.29 \mathrm{e}-3$ | $4.2 \mathrm{e}-5$ | $3.46 \mathrm{e}-3$ |
| $\theta_{1}$ | -.612e-2 | $6.77 \mathrm{e}-2$ | . 14 | $1.04 \mathrm{e}-2$ | -. 121 | $4.32 \mathrm{e}-2$ | 2.11 | . 212 |
| $\lambda_{01}$ | 3.84 | . 101 | 1.607 | $2.65 \mathrm{e}-2$ | 2.23 | . 171 | 2.062 | . 285 |
| $\lambda_{10}$ | 1.13 | . 148 | 4.369 | $4.13 \mathrm{e}-2$ | 3.156 | . 462 | 3.019 | . 618 |
| $p$ | . 368 | $8.63 \mathrm{e}-3$ | . 321 | $2.08 \mathrm{e}-3$ | . 394 | . 243 | . 952 | . 458 |
| Parameters | INTC | (se) | JNJ | (se) | MCD | (se) | MMM | (se) |
| $\sigma_{0}$ | . 409 | 3.19e-2 | . 236 | 1.3e-3 | . 497 | 1.03e-2 | . 217 | $7.08 \mathrm{e}-3$ |
| $\nu_{0}$ | $1.66 \mathrm{e}-3$ | $4.07 \mathrm{e}-3$ | $3.25 \mathrm{e}-3$ | $1.14 \mathrm{e}-3$ | $2.92 \mathrm{e}-3$ | $5.91 \mathrm{e}-3$ | $1.84 \mathrm{e}-3$ | $7.34 \mathrm{e}-4$ |
| $\theta_{0}$ | . 159 | $7.12 \mathrm{e}-1$ | . 106 | 1.51e-2 | . 489 | $3.27 \mathrm{e}-2$ | $3.57 \mathrm{e}-2$ | $1.29 \mathrm{e}-2$ |
| $\sigma_{1}$ | . 302 | $5.88 \mathrm{e}-2$ | . 24 | $2.65 \mathrm{e}-4$ | . 219 | $5.67 \mathrm{e}-3$ | . 433 | $5.75 \mathrm{e}-3$ |
| $\nu_{1}$ | $4.4 \mathrm{e}-5$ | $2.12 \mathrm{e}-3$ | $1.4 \mathrm{e}-4$ | $8.58 \mathrm{e}-4$ | $9.39 \mathrm{e}-4$ | $7.09 \mathrm{e}-4$ | $1.95 \mathrm{e}-3$ | $7.92 \mathrm{e}-3$ |
| $\theta_{1}$ | . 42 | $3.47 \mathrm{e}-2$ | . 103 | $8.61 \mathrm{e}-3$ | $1.66 \mathrm{e}-2$ | $2.44 \mathrm{e}-2$ | -3.44 | 8.1e-3 |
| $\lambda_{01}$ | 2.668 | . 239 | 2.627 | $3.89 \mathrm{e}-4$ | 2.424 | $2.66 \mathrm{e}-2$ | 1.562 | $1.84 \mathrm{e}-3$ |
| $\lambda_{10}$ | 3.977 | . 192 | 1.747 | $3.47 \mathrm{e}-2$ | 3.434 | . 3 | 3.894 | $9.59 \mathrm{e}-4$ |
| $p$ | . 598 | . 164 | . 499 | $7.33 \mathrm{e}-3$ | $6.49 \mathrm{e}-2$ | $9.97 \mathrm{e}-2$ | . 969 | $7.04 \mathrm{e}-3$ |


Note: Presented are maximum likelihood estimates of the parameters of a Markov chain model that moves between two VG processes seen as states. Mean corrected returns under each VG process are distributed as $\theta_{i}\left(g_{i}-t\right)+\sigma_{i} \sqrt{g_{i}} Z$, where $Z$ is a standard normal variate and $g_{i}$ is a gamma variate with mean $t$ and variance $\nu_{i} t$. The parameters $\lambda_{01}, \lambda_{10}$ are the state transition probabilities while $p$ is the initial probability of state 0 . Standard errors are in columns labeled (se). Estimates are for a sample of individual names. The data period is January 3, 1994 to December 9, 1998.
and February). The alternate state is however one with a low $\sigma$ but high values for $\nu$ the volatility of the pure jump time change. The market therefore reflects a chance of moving to a state with a significantly strengthened jump component and staying there for some time (witnessed by the low return transition probabilities). Such a view may be consistent with the length of the bull market at the time.

For a view of the overall performance of the non-linear least squares fit, we present in Figures 10 and 11 graphs of the data on implied volatilities and the two-stateVG Markov fit to this data.

## 8. Conclusion

An analysis of the term structure of risk neutral moments and interarrival times of market movements revealed a sharp inadequacy in the ability of homogeneous Lévy processes to explain the statistical and risk neutral price process for financial market prices. Noting the

Table 3(a). Single NameTwo-State VG Markov Parameter Estimates (Continued)
| Parameters | MRK | (se) | MSFT | (se) | UAL | (se) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\sigma_{0}$ | . 295 | 4.1e-3 | . 354 | $2.75 \mathrm{e}-2$ | . 447 | 1.96e-2 |
| $\nu_{0}$ | $2.02 \mathrm{e}-3$ | $1.6 \mathrm{e}-3$ | $6.91 \mathrm{e}-4$ | $6.58 \mathrm{e}-4$ | $2.01 \mathrm{e}-4$ | $6.26 \mathrm{e}-4$ |
| $\theta_{0}$ | $3.33 \mathrm{e}-2$ | $2.7 \mathrm{e}-3$ | . 718 | $5.92 \mathrm{e}-3$ | 1.224 | $1.02 \mathrm{e}-2$ |
| $\sigma_{1}$ | . 217 | $2.4 \mathrm{e}-3$ | . 197 | $8.55 \mathrm{e}-4$ | . 251 | $7.14 \mathrm{e}-3$ |
| $\nu_{1}$ | $1.6 \mathrm{e}-5$ | 1e-3 | $2 \mathrm{e}-6$ | $1.6 \mathrm{e}-4$ | 7.3e-5 | 9.65e-4 |
| $\theta_{1}$ | $2.81 \mathrm{e}-2$ | $1.97 \mathrm{e}-2$ | -. 765 | $2.24 \mathrm{e}-2$ | -. 349 | $2.52 \mathrm{e}-2$ |
| $\lambda_{01}$ | . 464 | $4.8 \mathrm{e}-3$ | 1.48 | $2.62 \mathrm{e}-2$ | 8.176 | $4.67 \mathrm{e}-2$ |
| $\lambda_{10}$ | 1.88 | $7.27 \mathrm{e}-2$ | . 924 | $5.95 \mathrm{e}-2$ | 1.295 | $3.29 \mathrm{e}-2$ |
| $p$ | . 499 | . 114 | . 798 | $8.79 \mathrm{e}-3$ | . 464 | $5.76 \mathrm{e}-2$ |
| Parameters | WMT | (se) | XON | (se) | YHOO | (se) |
| $\sigma_{0}$ | . 416 | $2.53 \mathrm{e}-2$ | . 218 | 9.93e-3 | . 78 | . 152 |
| $\nu_{0}$ | $4.07 \mathrm{e}-3$ | $4.08 \mathrm{e}-3$ | $1.43 \mathrm{e}-3$ | $5.98 \mathrm{e}-4$ | $2 \mathrm{e}-3$ | $2.62 \mathrm{e}-3$ |
| $\theta_{0}$ | $1.5 \mathrm{e}-2$ | . 154 | . 108 | $3.35 \mathrm{e}-2$ | 2.442 | . 343 |
| $\sigma_{1}$ | . 268 | $8.91 \mathrm{e}-4$ | . 317 | $3.83 \mathrm{e}-2$ | . 302 | $8.36 \mathrm{e}-2$ |
| $\nu_{1}$ | $3.2 \mathrm{e}-5$ | $7.48 \mathrm{e}-4$ | $5.16 \mathrm{e}-3$ | $1.72 \mathrm{e}-2$ | $1.98 \mathrm{e}-3$ | $1.84 \mathrm{e}-3$ |
| $\theta_{1}$ | $6.48 \mathrm{e}-2$ | $4.88 \mathrm{e}-2$ | -2.219 | $1.56 \mathrm{e}-2$ | -1.106 | . 321 |
| $\lambda_{01}$ | 5.421 | $6.57 \mathrm{e}-2$ | 2.56 | $3.19 \mathrm{e}-2$ | 9.6 | 1.129 |
| $\lambda_{10}$ | 5.811 | . 11 | 2.996 | $2.03 \mathrm{e}-2$ | 7.36 | 1.714 |
| $p$ | . 192 | . 176 | . 991 | $3.63 \mathrm{e}-2$ | . 498 | . 567 |


Note: Presented are maximum likelihood estimates of the parameters of a Markov chain model that moves between two VG processes seen as states. Mean corrected returns under each VG process are distributed as $\theta_{i}\left(g_{i}-t\right)+\sigma_{i} \sqrt{g_{i}} Z$, where $Z$ is a standard normal variate and $g_{i}$ is a gamma variate with mean $t$ and variance $\nu_{i} t$. The parameters $\lambda_{01}, \lambda_{10}$ are the state transition probabilities while $p$ is the initial probability of being in state 0 . Standard errors are in columns labeled (se). The estimates are for a sample of individual names. The data period is January 3, 1994 to December 9, 1998.
closeness of a model mixing two exponentials in empirically explaining interarrival times over a hundred years, we developed a two-state Markov model for the price process that builds volatility clustering by jumping between these two states. For this stochastic process we present closed form expressions for the characteristic function and show how these may be coupled with the applications of the Fast Fourier transform to render feasible parameter estimation of the statistical process by maximum likelihood and calibration to the options surface simultaneously over all strikes and an initial segment of maturities. The results are both promising and interesting. The homogeneous Lévy processes we employ are the three parameter variance gamma process and we observe significant improvements rendered by the two-state variance gamma Markov model. The methods developed can be employed to construct chains across other Lévy processes just as easily.

For the period studied the statistical process is consistent with a high probability of being in a less risky environment with a move to a more risky environment likely. The risk neutral process varies with the underlying and for IBM and INTC it reflects the possibility

Table 3(b). Two-State VG Markov Parameter Estimates for Market Indices
| Parameters | BIX | (se) | BKX | (se) | DRG | (se) | RUT | (se) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\sigma_{0}$ | . 276 | 3.81e-4 | . 271 | $9.06 \mathrm{e}-4$ | . 179 | 1e-2 | . 163 | $1.67 \mathrm{e}-2$ |
| $\nu_{0}$ | $4.16 \mathrm{e}-3$ | $9.24 \mathrm{e}-4$ | $4.71 \mathrm{e}-3$ | $5.81 \mathrm{e}-4$ | $1.86 \mathrm{e}-3$ | $8.03 \mathrm{e}-4$ | $4.76 \mathrm{e}-3$ | $1.97 \mathrm{e}-3$ |
| $\theta_{0}$ | $2.19 \mathrm{e}-2$ | $1.01 \mathrm{e}-3$ | -. 252 | $2.29 \mathrm{e}-3$ | . 07 | $5.48 \mathrm{e}-2$ | $-3.9 \mathrm{e}-3$ | $8.07 \mathrm{e}-4$ |
| $\sigma_{1}$ | . 171 | $1.63 \mathrm{e}-3$ | . 174 | $1.76 \mathrm{e}-5$ | . 302 | $1.33 \mathrm{e}-2$ | $8.47 \mathrm{e}-2$ | $4.94 \mathrm{e}-3$ |
| $\nu_{1}$ | $2.11 \mathrm{e}-4$ | $7.48 \mathrm{e}-4$ | $1.3 \mathrm{e}-4$ | $2.2 \mathrm{e}-4$ | $1.93 \mathrm{e}-2$ | $1.74 \mathrm{e}-2$ | $9.73 \mathrm{e}-4$ | $2.12 \mathrm{e}-3$ |
| $\theta_{1}$ | . 159 | $4.12 \mathrm{e}-3$ | . 318 | $1.54 \mathrm{e}-3$ | -1.357 | . 105 | $-4.49 \mathrm{e}-2$ | $2.4 \mathrm{e}-2$ |
| $\lambda_{01}$ | 1.138 | $6.74 \mathrm{e}-3$ | 1.774 | $3.18 \mathrm{e}-3$ | 1.371 | $5.45 \mathrm{e}-2$ | 8.065 | $2.69 \mathrm{e}-2$ |
| $\lambda_{10}$ | 4.444 | $2.12 \mathrm{e}-2$ | 2.735 | $1.65 \mathrm{e}-2$ | 3.038 | . 104 | 3.41 | $1.68 \mathrm{e}-3$ |
| $p$ | . 359 | $3.45 \mathrm{e}-2$ | . 414 | $3.54 \mathrm{e}-2$ | . 967 | $8.25 \mathrm{e}-2$ | . 499 | $7 \mathrm{e}-4$ |
| Parameters | SOX | (se) | SPX | (se) | XAU | (se) | XOI | (se) |
| $\sigma_{0}$ | . 265 | $4.58 \mathrm{e}-3$ | . 113 | 1.9e-3 | . 283 | $1.77 \mathrm{e}-2$ | . 189 | $2.06 \mathrm{e}-5$ |
| $\nu_{0}$ | $4.4 \mathrm{e}-5$ | $1.67 \mathrm{e}-3$ | $5.6 \mathrm{e}-4$ | $2.4 \mathrm{e}-3$ | $6.8 \mathrm{e}-5$ | 7.6e-4 | $1.39 \mathrm{e}-3$ | $2 \mathrm{e}-5$ |
| $\theta_{0}$ | . 135 | $2.7 \mathrm{e}-2$ | . 217 | $3.98 \mathrm{e}-2$ | -. 76 | 3.3e-2 | $6.24 \mathrm{e}-3$ | $1.18 \mathrm{e}-4$ |
| $\sigma_{1}$ | . 451 | $4.97 \mathrm{e}-2$ | . 186 | $1 \mathrm{e}-4$ | . 593 | $2.16 \mathrm{e}-2$ | $9.66 \mathrm{e}-2$ | $9.96 \mathrm{e}-6$ |
| $\nu_{1}$ | 3.3e-4 | $7.71 \mathrm{e}-4$ | $8.24 \mathrm{e}-3$ | $2 \mathrm{e}-3$ | $6.85 \mathrm{e}-4$ | 3.8e-3 | $1.3 \mathrm{e}-5$ | 1.6le-6 |
| $\theta_{1}$ | . 122 | $7.15 \mathrm{e}-2$ | -. 205 | $8 \mathrm{e}-4$ | 1.43 | $8.48 \mathrm{e}-2$ | $-1.64 \mathrm{e}-4$ | $1.45 \mathrm{e}-4$ |
| $\lambda_{01}$ | 4.95 | . 21 | 9.184 | $2.68 \mathrm{e}-2$ | 2.018 | . 471 | 9.201 | $1.69 \mathrm{e}-4$ |
| $\lambda_{10}$ | 2.25 | $3.17 \mathrm{e}-2$ | 3.002 | $4.5 \mathrm{e}-2$ | 3.111 | . 668 | 3.102 | $1.58 \mathrm{e}-4$ |
| $p$ | . 387 | $7.74 \mathrm{e}-2$ | . 64 | $9 \mathrm{e}-3$ | . 797 | . 359 | . 61 | $1.35 \mathrm{e}-4$ |


Note: Presented are maximum likelihood estimates of the parameters of a Markov chain model that moves between two VG processes seen as states. Mean corrected returns under each VG process are distributed as $\theta_{i}\left(g_{i}-t\right)+\sigma-i \sqrt{g_{i}} \mathbf{Z}$ where $Z$ is a standard normal variate and $g_{i}$ is a gamma variate with mean $t$ and variance $\nu_{i} t$. The parameters $\lambda_{01}, \lambda_{10}$ are the state transition probabilities while $p$ is the initial probability of being in state 0 . Standard errors are in columns labeled (se). The estimates for a sample of market indices. The data period is January 3, 1994 to December 9, 1998.
of a move to a less risky environment while for the S\&P 500 index it reflects a move to a state with considerably higher moments.

## Appendix

## Proof of Proposition 1

The moment generating function for $X(t)$ has the form

$$
M_{X(t)}(u)=E\left[e^{u X(t)}\right]=m(u)^{t}
$$

where $m(u)=M_{X(1)}(u)$. Denote by $\mu_{j}$ the $j$ th root of the uncentralized $j$ th moment of $X(1)$ or

$$
\mu_{j}^{j}=E\left(X(1)^{j}\right)=m^{(j)}(0) .
$$

Table 4. Likelihood Ratio Tests of GBM Versus VG and VG Versus the Two State VG Markov (VGM) Model
| Ticker | BS LL | VG LL | LLR | VGM LL | LLR | $\chi_{1}^{20 \%}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BA | 3285 | 3350.4 | 130.8 | 3358 | 15.19 | 100 |
| BIX | 3637.1 | 3701.1 | 128 | 3708.47 | 14.74 | 100 |
| BKX | 3605.89 | 3672.46 | 133.14 | 3679.12 | 13.33 | 100 |
| DGR | 3801.23 | 3868.2 | 133.94 | 3875.34 | 14.27 | 100 |
| GE | 3510.1 | 3541 | 61.81 | 3547.41 | 12.83 | 100 |
| HWP | 2960.43 | 3034.3 | 147.74 | 3043.4 | 18.2 | 100 |
| IBM | 3164.93 | 3247.1 | 164.34 | 3262.18 | 30.17 | 100 |
| INTC | 2956.41 | 2986.6 | 60.38 | 2991.57 | 9.94 | 100 |
| JNJ | 3508.99 | 3525.54 | 33.11 | 3528.08 | 5.06 | 97.56 |
| MCD | 3448.48 | 3503 | 109.04 | 3513.24 | 20.47 | 100 |
| MMM | 3534.02 | 3588.91 | 109.77 | 3592.93 | 8.05 | 100 |
| MRK | 3393.22 | 3424.7 | 62.96 | 3428.86 | 8.32 | 100 |
| MSFT | 3092.59 | 3109.07 | 32.96 | 3110.34 | 2.54 | 88.91 |
| RUT | 4246.9 | 4389.2 | 284.61 | 4401.47 | 24.54 | 100 |
| SOX | 2886.65 | 2898.07 | 22.84 | 2900.29 | 4.44 | 96.49 |
| SPX | 4125.66 | 4245.3 | 239.29 | 4257.34 | 24.08 | 100 |
| UAL | 2990 | 3004.52 | 29.04 | 3006.94 | 4.84 | 97.23 |
| WMT | 3191.05 | 3225.5 | 68.89 | 3233.22 | 15.43 | 100 |
| XAU | 2938.72 | 2981.8 | 86.16 | 2998.13 | 32.66 | 100 |
| XOI | 4014.75 | 4055.67 | 81.85 | 4057.26 | 3.18 | 92.53 |
| XON | 3635.38 | 3659.7 | 48.64 | 3661.03 | 2.65 | 89.66 |
| YHOO | 2424.64 | 2536.1 | 222.92 | 2543.49 | 14.78 | 100 |


Note: Likelihoods as well as likelihood ratio test statistics are presented for the two nested hypotheses of the GBM model versus the VG and the VG model versus the VGM model. The final column contains the $\chi_{1}^{2}$ probability level for the VGM/VG likelihood ratio. The data period is January 3, 1994 to December 9, 1998.

It follows on differentiation that

$$
\begin{aligned}
E[X(t)]= & t \mu_{1} \\
E\left[X(t)^{2}\right]= & t \mu_{2}^{2}+t(t-1) \mu_{1}^{2} \\
E\left[X(t)^{3}\right]= & t \mu_{3}^{3}+t(t-1)(t-2) \mu_{1}^{3}+3 t(t-1) \mu_{1} \mu_{2}^{2} \\
E\left[X(t)^{4}\right]= & 6 t(t-1)(t-2) \mu_{1}^{2} \mu_{2}^{2}+3 t(t-1) \mu_{2}^{4} \\
& +4 t(t-1) \mu_{1} \mu_{3}^{3}+t \mu_{4}^{4}+t(t-1)(t-2)(t-3) \mu_{1}^{4}
\end{aligned}
$$

The centralized higher moments are

$$
\begin{aligned}
& E\left[(X(t)-E(X(t)))^{2}\right]=t\left(\mu_{2}^{2}-\mu_{1}^{2}\right) \\
& E\left[(X(t)-E(X(t)))^{3}\right]=t\left(\mu_{3}^{3}+2 \mu_{1}^{3}-3 \mu_{1} \mu_{2}^{2}\right) \\
& E\left[(X(t)-E(X(t)))^{4}\right]=t\left[12 \mu_{1}^{2} \mu_{2}^{2}-3 \mu_{2}^{4}-4 \mu_{1} \mu_{3}^{3}+\mu_{4}^{4}-6 \mu_{1}^{4}\right]+3 t^{2}\left(\mu_{2}^{2}-\mu_{1}^{2}\right)^{2} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-29.jpg?height=743&width=904&top_left_y=551&top_left_x=593)
Figure 7. Observed and estimated likelihoods for BA . Shown are the observed binned likelihood and the VG and two-state Markov VG fitted densities for BA. The circles represent the observed probability while the solid and dashed lines are the fitted two state VG and VG densities.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-29.jpg?height=747&width=909&top_left_y=1484&top_left_x=593)
Figure 8. Observed and estimated likelihoods for HWP. Shown are the observed binned likelihood and the VG and two-state Markov VG fitted densities for HWP. The circles represent the observed probability while the solid and dashed lines are the fitted two state VG and VG densities.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-30.jpg?height=743&width=898&top_left_y=551&top_left_x=596)
Figure 9. Observed and estimated likelihoods for SPX. Shown are the observed binned likelihood and the VG and two-state Markov VG fitted densities for SPX. The circles represent the observed probability while the solid and dashed lines are the fitted two state VG and VG densities.

Table 5(a). Risk Neutral Estimates of the Two State VG Markov Model for SPX

|  | Oct. 14 | Nov. 11 | Dec. 9 | Jan. 13 | Jan. 13 | Feb. 10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| No. of | 3 | 3 | 3 | 3 | 4 | 3 |
| Maturities |  |  |  |  |  |  |
| $\sigma_{0}$ | . 387 | . 227 | . 198 | . 363 | . 446 | . 249 |
| $\nu_{0}$ | . 034 | . 088 | . 06 | . 028 | . 016 | . 045 |
| $\theta_{0}$ | -. 919 | -. 589 | -. 463 | -1.789 | -1.721 | -. 828 |
| $\sigma_{1}$ | . 086 | $7.53 \mathrm{e}-3$ | . 062 | . 196 | . 182 | . 064 |
| $\nu_{1}$ | . 836 | . 999 | . 454 | . 038 | . 05 | . 484 |
| $\theta_{1}$ | -. 508 | -. 34 | -. 552 | -. 335 | -. 372 | -. 498 |
| $\lambda_{01}$ | 6.334 | 6.097 | 5.707 | 3.096 | 3.302 | 5.671 |
| $\lambda_{10}$ | . 085 | . 007 | $6.16 \mathrm{e}-3$ | $2.61 \mathrm{e}-3$ | $2.3 \mathrm{e}-3$ | $1.57 \mathrm{e}-4$ |
| $p$ | . 807 | . 9992 | . 9985 | . 178 | . 194 | . 9985 |
| Relative Error | . 0327 | . 0723 | . 0664 | . 0783 | . 0868 | . 0846 |

Note: Parameter estimates of the two state VG Markov model estimated on SPX options for five days are presented. The two VG states are described by Brownian motion with drift $\theta_{i}$ and volatility $\sigma_{i}$ time changed by a gamma process with mean $t$ and variance $\nu_{i} t$. The state transition probabilities are $\lambda_{01}, \lambda_{10}$ while $p$ is the initial probability of state 0 . Also shown are the number of maturities simultaneously calibrated as well as the average absolute percentage error.

It follows that

$$
\operatorname{variance}_{X(t)}=\left(\mu_{2}^{2}-\mu_{1}^{2}\right) t
$$

Table 5(b). Risk Neutral Estimates of the Two State VG Markov Model for IBM
|  | Oct. 14 | Nov. 11 | Dec. 9 | Jan. 13 | Jan. 13 | Feb. 10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| No. of | 5 | 5 | 5 | 3 | 5 | 5 |
| Maturities |  |  |  |  |  |  |
| $\sigma_{0}$ | . 036 | . 275 | . 225 | . 19 | . 166 | . 296 |
| $\nu_{0}$ | . 214 | . 261 | . 069 | . 01 | . 291 | . 0523 |
| $\theta_{0}$ | -. 0365 | -. 224 | -. 132 | -. 601 | -. 148 | -. 519 |
| $\sigma_{1}$ | . 582 | . 384 | . 457 | . 489 | . 557 | . 5 |
| $\nu_{1}$ | . 081 | . 44 | . 384 | . 033 | . 087 | . 084 |
| $\theta_{1}$ | -. 887 | -. 328 | -. 325 | -. 934 | -. 316 | -. 69 |
| $\lambda_{01}$ | . 95 | 1.983 | 1.95 | 1.116 | 1.84 | 1.482 |
| $\lambda_{10}$ | 3.654 | 3.012 | 3.03 | 3.609 | 3.096 | 3.326 |
| $p$ | . 245 | . 503 | . 498 | . 271 | . 448 | . 335 |
| Relative Error | . 0284 | . 0734 | . 0784 | . 0282 | . 0909 | . 0469 |


Note: Parameter estimates of the two state VG Markov model estimated on IBM option for five days are presented. The two VG states are described by Brownian motion with drift $\theta_{i}$ and volatility $\theta_{i}$ time changed by a gamma process with mean $t$ and variance $\nu_{i} t$. The state transition probabilities are $\lambda_{01}, \lambda_{10}$ while $p$ is the initial probability of state 0 . Also shown are the number of maturities simultaneously calibrated as well as the average absolute percentage error.

Table 5(c). Risk Neutral Estimates of the Two State VG Markov Model for INTC
|  | Oct. 14 | Nov. 11 | Dec. 9 | Jan. 13 | Feb. 10 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| No. of Maturities | 5 | 5 | 5 | 5 | 5 |
| $\sigma_{0}$ | . 279 | . 242 | . 248 | . 309 | . 319 |
| $\nu_{0}$ | . 108 | . 06 | . 035 | . 094 | . 14 |
| $\theta_{0}$ | -. 381 | -. 383 | -. 377 | -. 516 | -. 492 |
| $\sigma_{1}$ | . 56 | . 479 | . 519 | . 511 | . 566 |
| $\nu_{1}$ | . 207 | . 136 | . 087 | . 047 | . 057 |
| $\theta_{1}$ | -. 581 | -. 523 | -. 512 | -. 482 | -. 529 |
| $\lambda_{01}$ | 2.468 | 2.465 | 2.465 | 2.477 | 1.469 |
| $\lambda_{10}$ | 3.526 | 3.529 | 3.529 | 3.516 | 2.521 |
| $p$ | . 402 | . 404 | . 403 | . 396 | . 393 |
| Relative Error | . 0753 | . 0703 | . 0692 | . 0804 | . 0828 |


Note: Parameter estimates of the two state VG Markov model estimated on INTC option for five days are presented. The two VG states are described by Brownian motion with drift $\theta_{i}$ and volatility $\sigma_{i}$ time changed by a gamma process with mean $t$ and variance $\nu_{i} t$. The state transition probabilities are $\lambda_{01}, \lambda_{10}$ while $p$ is the initial probability of state 0 . Also shown are the number of maturities simultaneously calibrated as well as the average absolute percentage error.

$$
\begin{aligned}
\text { skewness }_{X(t)} & =\frac{\mu_{3}^{3}+2 \mu_{1}^{3}-3 \mu_{1} \mu_{2}^{2}}{\left(\mu_{2}^{2}-\mu_{1}^{2}\right)^{3 / 2}} \frac{1}{\sqrt{t}} \\
\text { kurtosis }_{X(t)}-3 & =\frac{12 \mu_{1}^{2} \mu_{2}^{2}-3 \mu_{2}^{4}-4 \mu_{1} \mu_{3}^{3}+\mu_{4}^{4}-6 \mu_{1}^{4}}{\left(\mu_{2}^{2}-\mu_{1}^{2}\right)^{2}} \frac{1}{t} .
\end{aligned}
$$

Table 5(d). Risk Neutral Estimates of the Two State VG Markov Model for MSFT
|  | Oct. 14 | Nov. 11 | Dec. 9 | Jan. 13 | Feb. 10 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| No. of Maturities | 3 | 3 | 3 | 3 | 3 |
| $\sigma_{0}$ | . 631 | . 255 | . 444 | . 505 | . 504 |
| $\nu_{0}$ | . 035 | . 084 | . 108 | . 008 | . 007 |
| $\theta_{0}$ | -1.318 | -. 054 | -. 45 | -. 582 | -. 582 |
| $\sigma_{1}$ | . 288 | . 434 | . 328 | . 438 | . 402 |
| $\nu_{1}$ | . 01 | . 071 | . 085 | . 207 | . 108 |
| $\theta_{1}$ | -. 428 | -. 51 | -. 268 | -. 256 | -. 41 |
| $\lambda_{01}$ | 6.149 | . 13 | 6.895 | 17.868 | 18.042 |
| $\lambda_{10}$ | . 332 | 1.537 | . 742 | . 321 | . 2311 |
| $p$ | . 994 | . 405 | . 99 | . 94 | . 93 |
| Relative Error | . 0326 | . 0448 | . 0318 | . 076 | . 0612 |


Note: Parameter estimates of the two state VG Markov model estimated on MSFT option for five days are presented. The two VG states are described by Brownian motion with drift $\theta_{i}$ and volatility $\sigma_{i}$ time changed by a gamma process with mean $t$ and variance $\nu_{i} t$. The state transition probabilities are $\lambda_{01}, \lambda_{10}$ while $p$ is the initial probability of state 0 . Also shown are the number of maturities simultaneously calibrated as well as the average absolute percentage error.

Table 5(e). Risk Neutral Estimates of the Two State VG Markov Model for YHOO
|  | Oct. 14 | Nov. 11 | Dec. 9 | Jan. 13 |
| :--- | :--- | :--- | :--- | :--- |
| No. of Maturities | 3 | 3 | 3 | 3 |
| $\sigma_{0}$ | . 816 | . 788 | 1.076 | 1.127 |
| $\nu_{0}$ | . 019 | . 062 | . 939 | . 053 |
| $\theta_{0}$ | -. 867 | -. 636 | -. 897 | -1.321 |
| $\sigma_{1}$ | . 466 | . 118 | . 889 | 1.104 |
| $\nu_{1}$ | 3.11 | 2.936 | . 075 | . 113 |
| $\theta_{1}$ | -. 47 | -. 582 | -1.239 | -1.24 |
| $\lambda_{01}$ | 4.682 | 1.481 | 5.125 | 6.513 |
| $\lambda_{10}$ | 5.935 | 1.896 | 6e-4 | . 614 |
| $p$ | . 989 | . 988 | $2 \mathrm{e}-5$ | . 953 |
| Relative Error | . 0735 | . 0796 | . 0934 | . 072 |


Note: Parameter estimates of the two state VG Markov model estimated on YHOO option for five days are presented. The two VG states are described by Brownian motion with drift $\theta_{i}$ and volatility $\sigma_{i}$ time changed by a gamma process with mean $t$ and variance $\nu_{i} t$. The state transition probabilities are $\lambda_{01}, \lambda_{10}$ while $p$ is the initial probability of state 0 . Also shown are the number of maturities simultaneously calibrated as well as the average absolute percentage error.

## Proof of Proposition 3

Let $q_{T}(s)$ denote the risk neutral density for the log of the stock price at time $T$. By the principle of risk neutral valuation we have that

$$
z_{T}(k)=\mathbf{1}_{\ln \left(F_{0}\right)<k} e^{-r T} \int_{k}^{\infty}\left(e^{s}-e^{k}\right) q_{T}(s) d s-\mathbf{1}_{\ln \left(F_{0}\right)>k} e^{-r T} \int_{-\infty}^{k}\left(e^{s}-e^{k}\right) q_{T}(s) d s
$$

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-33.jpg?height=709&width=886&top_left_y=542&top_left_x=571)
Figure 10. Observed and fitted implied volatilities for IBM. Shown are the observed implied volatilities and the fitted two-state VG Markov implied volatilities for IBM on October 14, 1998. Circles indicate the observed implied volatilities for the various maturities while the solid lines are the implied volatilities derived from the two state Markov model fit to all maturities simultaneously.

![](https://cdn.mathpix.com/cropped/2025_11_24_37947e2fc69ed20e960bg-33.jpg?height=709&width=886&top_left_y=1496&top_left_x=571)
Figure 11. Observed and fitted implied volatilities for IBM. Shown are the observed implied volatilities and the fitted two-state VG Markov implied volatilities for IBM on November 11, 1998. Circles indicate the observed implied volatilities for the various maturities while the solid lines are the implied volatilities derived from the two state Markov model fit to all maturities simultaneously.

It follows that

$$
\begin{aligned}
\zeta_{T}(v)= & e^{-r T}\left[\int_{\ln \left(F_{0}\right)}^{\infty} e^{i v k} \int_{k}^{\infty}\left(e^{s}-e^{k}\right) q_{T}(s) d s d k\right] \\
& -e^{-r T}\left[\int_{-\infty}^{\ln \left(F_{0}\right)} e^{i v k} \int_{-\infty}^{k}\left(e^{s}-e^{k}\right) q_{T}(s) d s d k\right] \\
= & e^{-r T}\left[\int_{\ln \left(F_{0}\right)}^{\infty} q_{T}(s) \int_{\ln \left(F_{0}\right)}^{s}\left(e^{s+i v k}-e^{(1+i v) k}\right) d s d k\right] \\
& -e^{-r T}\left[\int_{-\infty}^{\ln \left(F_{0}\right)} q_{T}(s) \int_{s}^{\ln \left(F_{0}\right)}\left(e^{s+i v k}-e^{(1+i v) k}\right) d k d s\right] \\
= & e^{-r T} \int_{-\infty}^{\infty} q_{T}(s)\left(\frac{e^{(1+i v) s}-e^{s} F_{0}^{i v}}{i v}-\frac{e^{(1+i v) s}-F_{0}^{(1+i v)}}{1+i v}\right) d s \\
= & e^{-r T}\left[\frac{F_{0}^{1+i v}}{1+i v}-\frac{\phi_{\ln (S(T))}(v-i)}{v(v-i)}-\frac{F_{0}^{1+i v}}{i v}\right] \\
= & e^{-r T}\left[\frac{F_{0}^{1+i v}-\phi_{\ln (S(T))}(v-i)}{v(v-i)}\right] .
\end{aligned}
$$

## Notes

1. We note in passing that this is a dynamic yard stick as the spreads fall with the expansion of electronic trading and the enhanced liquidity.
2. We are indebted to Darrell Duffie and Robert Elliott for discussions relating to this solution.

## Acknowledgements

The authors are indebted to Peter Carr and Ajay Khanna for innumerable discussions and much encouragements and Darrell Duffie and Robert Elliott for assistance on a technical point. Errors remain our responsibility.

## References

Andersen, T. G. (1994). "Stochastic Autoregressive Volatility: A Framework for Volatility Modeling," Mathematical Finance 4, 75-102.
Andé, T., and H. Geman. (2000). "Order Flow, Transaction Clock and Normality of Asset Returns," Journal of Finance 55, 2259-2284.
Bakshi, G., C. Cao, and Z. Chen. (1997). "Empirical Performance of Altrernative Option Pricing Models," Journal of Finance 52, 2003-2049.

Barndorff-Nielsen, O. (1998). "Processes of Normal Inverse Gaussian Type," Finance and Stochastics 2, 41-68.
Barndorff-Nielsen, O., and N. Shephard. (1999). "Non-Gaussian OU Based Models and Some of Their Uses in Financial Economics," Working Paper No. 37, Center for Analytical Finance, University of Aarhus.
Bates, D. (1996). "Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutschemark Options," Review of Financial Studies 9, 69-108.
Black, F., and M. Scholes. (1973). "The Pricing of Options and Corporate Liabilities," Journal of Political Economy 81, 637-654.
Carr, P., H. Geman, D. Madan, and M. Yor. (2000). "The Fine Structure of Asset Returns: An Empirical Investigation," forthcoming in the Journal of Business.
Carr, P., H. Geman, D. Madan, and M. Yor. (2001). "Stochastic Volatility for Lévy Processes," Working Paper, University of Maryland.
Carr, P., and D. B. Madan. (1999). "Option Valuation Using the Fast Fourier Transform," Journal of Computational Finance 1, 61-73.
Clark, P. K. (1973). "A Subordinated Stochastic Process Model with Finite Variance for Speculative Prices," Econometrica 41, 135-156.
Derman, E., and I. Kani. (1998). "Stochastic Implied Trees: Arbitrage Pricing with Stochastic Term and Strike Structure of Volatility," International Journal of Theoretical and Applied Finance 3, 7-22.
Dupire, B. (1994). "Pricing With a Smile," Risk 7, 1, 18-20.
Duan, J, I. Popova, and P. Ritchken. (1999). "Option Pricing under Regime Switching," Working Paper, Case Western Reserve University.
Eberlein, E., U. Keller, and K. Prause. (1998). "New Insights into Smile, Mispricing and Value at Risk: The Hyperbolic Model," Journal of Business 71, 371-406.
Elliott, Robert J., Lakhdar Aggoun, and John B. Moore. (1995). Hidden Markov Models: Estimation and Control (Applications of Mathematics, Vol. 29). Berlin: Springer-Verlag.
Engle, R. F. (1982). "Autoregressive Conditional Heteroskedasticity with Estimates of the Variance of United Kingdom Inflation," Econometrica, 61, 929-952.
Geman, H., D. Madan, and M. Yor. (2001). "Time Changes for Lévy Processes," Mathematical Finance 11, 79-96.
Heston, S. L. (1993). "A Closed Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options," Review of Financial Studies 6, 327-343.
Madan, D. B., and E. Seneta. (1990). "The Variance Gamma (VG) Model for Share Market Returns," Journal of Business 63, 4, 511-524.
Madan, D. B., P. P. Carr, and E. C. Chang. (1998). "The Variance Gamma Process and Option Pricing," European Finance Review 2, 79-105.
Merton, R. C. (1973). "Theory of Rational Option Pricing," Bell Journal of Economics and Management 4, 141-183.
Merton, R. C. (1976). "Option Pricing when Underlying Stock Returns are Discontinuous," Journal of Financial Economics 3, 125-144
Nelson, D. (1991). "Conditional Heteroskedasticity in Asset Returns: A NewApproach," Econometrica 59,347-370.

