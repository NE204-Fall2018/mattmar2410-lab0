import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from modelling import gauss
import statsmodels.api as sm
from lmfit.models import GaussianModel
from lmfit.models import LinearModel

def spectrum_calibration(channel_width, energy_list, data_2_calibrate):

    '''
    The while loop goes through and identifies the largest peak in the
    spectrum and it records the position of that peak. It then removes
    the peak by removing 10 channels from the right and left of the peak.
    The code will then search for the next largest position.
    '''

    i = 0; channel_max_list = []; gauss_x = []; gauss_y = []
    fit_channel = []; channel_std_list = []
    while i < len(energy_list):
        channel_max = np.argmax(data_2_calibrate)
        #channel_max_list.append(channel_max)
        data_left = channel_max - channel_width
        data_right = channel_max + channel_width
        '''
        Instead of deleting the items from the list. I am placing them to
        zero. The while loop iterates over the peak and sets it to zero.
        '''
        iterator = data_left
        while iterator < (data_right):
            gauss_x.append(iterator)
            gauss_y.append(data_2_calibrate[iterator])
            x = np.asarray(gauss_x)
            y = np.asarray(gauss_y)
            fit_channel.append(data_2_calibrate[iterator])
            data_2_calibrate[iterator] = 0
            iterator += 1
        i += 1
        '''
        information for plotting the Gaussian function.
        '''
        mod  = GaussianModel(prefix='g1_')
        line_mod = LinearModel(prefix='line')
        pars = mod.guess(y, x=x)
        pars.update(line_mod.make_params(intercept=y.min(), slope=0))
        pars.update( mod.make_params())
        pars['g1_center'].set(gauss_x[np.argmax(gauss_y)], min=gauss_x[np.argmax(gauss_y)]\
        - 3)
        pars['g1_sigma'].set(3, min=0.25)
        pars['g1_amplitude'].set(max(gauss_y), min=max(gauss_y)-10)
        mod = mod + line_mod
        out  = mod.fit(y, pars, x=x)
        center = out.params['g1_center'].value
        center_std = out.params['g1_center'].stderr
        channel_max_list.append(center)
        channel_std_list.append(center_std)
        gauss_x = []; gauss_y = []; fit_channel = []

    '''
    sorting channel number so the correct channel number corresponds with
    the correct energy.
    '''
    channel_number = sorted(channel_max_list, key=int)
    channel_std = sorted(channel_std_list, key=int)
    energy = energy_list
    results = sm.OLS(energy,sm.add_constant(channel_number)).fit()

    slope, intercept = np.polyfit(channel_number, energy, 1)

    abline_values = [slope * i + intercept for i in channel_number]
    plt.figure()
    plt.errorbar(channel_number, energy, channel_std, marker = 'o', linestyle=None)
    plt.plot(channel_number, abline_values)
    plt.xlabel('Channel Number')
    plt.ylabel('Energy [keV]')
    plt.title('Best Fit Line $y=%3.7sx+%3.7s$' % (slope, intercept), fontsize=16)
    plt.savefig('../images/best_fit_line.png')
    return slope, intercept
