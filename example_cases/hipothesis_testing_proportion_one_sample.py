
# Further information: https://sonalake.com/latest/hypothesis-testing-of-proportion-based-samples/
# Also https://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html

from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as st
import pandas as pd

# df = pd.read_csv('../data/airline_passenger_satisfaction.csv')
df = pd.read_csv('data/airline_passenger_satisfaction.csv')

sample_size = 100
significance = 0.95
null_hypothesis = 0.5
df_sample = df.sample(n=sample_size)

sample_success = df_sample.query("`Type of Travel` == 'Business'").__len__()

proportions_ztest(count=sample_success,
                  nobs=sample_size,
                  value=null_hypothesis,
                  alternative='two-sided'
                  )


if __name__ == '__main__':
    pass




#
#
# ——————————— ——————————— ——————————— ———————————
#
# 1. Popraviti grafikon, izbaciti legendu.
# 2. Ubaciti grafikon sa t raspodelom (kod normalne raspodele).
# 3.
#
#
#
#
# Part I)
# Ivana ce poslati text:
# Sta je statistika?
# Cilj statistike.
# Osnovno pojmovi
# Tipi varijable
#
#
# Part II)
#
# Intro to dataset
# Prikaz sa tabelom
# - bin-sizes vizualizacija
# Data visualisation
#
# *** Ubacujem slike sa formulama za:
# 	- Poslace Ivana teze
# 	- I poslace slike Ivana
# 	- mean, variance, stdefv, mode, median (bez formule)
# 	- Izracunati vrednosti za varijable u skupu
# 	- Ubaciti sformule u markdown (mean, stdev, mode, mediana) I interakciju da Ivan klikne.
#
#
# III) Moje interaktivne vizualizacije.
#
# 	- central-limit-theorem
# 	- distributions
# 	- interactive-distributions
#
#
# IV) Confidence interval
#
# Interaktivna vizualizacija:
# - Zvonasta kriva, dve vertikalne linije koje predstavljaju interval poverenja,
# Parametre (, confidence level, velicia uzorka, sem) (PDF student distribution).
#
# *** Ako napravim MC simulaciju, ispričati logiku python kodova.
#
# V) Regresija - obicna I logistic
#
# Obicna regresija:
#
# 	- Slika sa linijom regresije (tackasti diagram)
# 	- Beta0, beta1
# 	- total/average Mean Square Error
# 	- value za beta1
# 	- coefficient of determination
#
#
# Logistic regresija:
# 	- general idea of clarification
# 	- zavisna varijabla - zadovoljstvo
# 	- nezavisne varijable
# 	- metrike klasifikacije
# 	- confuse metric
# 	- extra sexy and advanced example
# 	- testioranje beta koeficijenata
#
#
#
#
#






