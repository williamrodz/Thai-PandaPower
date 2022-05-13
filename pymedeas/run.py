#!/usr/bin/env python
__author__ = "Oleg Osychenko, Roger Samsó"
__maintainer__ = "Roger Samsó"
__status__ = "Development"

"""
This code allows parametrizing, launching and saving and plotting the results of the pymedeas_w.py and pymedeas_eu models.
"""

import plot_tool
from pytools.tools import *
import os
import time
import warnings
warnings.filterwarnings("ignore")


def main(model, config, run_params, **kwargs):

    for key, val in kwargs.items():
        config['update_params'].update({key: val})

    # create path for the python model file
    model_file = os.path.join(config['folder'], config['model_py'])

    # clearing the cache of components
    for comp in [element for element in dir(model.components) if
                 not element.startswith("_")]:
        if hasattr(getattr(model.components, comp), 'cache_val'):
            delattr(getattr(model.components, comp), 'cache_val')

    # Find updated parameters. Each tuple=(updated cell name, value of parameter)
    cells_updated = find_updated_cells(config)

    # looking for model parameters that need to be updated
    if cells_updated:
        not_ctts, updated_ctts = update_ctts(config, cells_updated)
        updated_mats = update_matrices(model, config,
                                       [cell for cell in not_ctts])
        config['update_params'].update({**updated_ctts, **updated_mats})
        updated_params_to_file(config, 'txt')

    # updating model components
    for parameter, value in config['update_params'].items():
        update_model_component(model, parameter, value)

    # list of columns that need to be present in the output file
    # TODO loading the model in utf should be avoided in further versions
    model_py = read_file(model_file, 'utf-8')
    return_columns = select_model_outputs(config, model_py)

    # reinitializing components
    # TODO replace dir(model.components) by model.components._namespace.values
    for comp in [element for element in dir(model.components) if
                 not element.startswith("_")]:
        if hasattr(getattr(model.components, comp), 'cache_val'):
            exec("model.components.{}()".format(comp))

    # reinitializing stateful elements (integrals, delays, etc)
    for element in model._stateful_elements:
        element.initialize()

    # run the simulation
    stock = run(config, model, run_params, return_columns)

    result_df = store_results_csv(stock, config, return_columns)

    # running the plot tool
    if config['plot']:
        if not config['headless']:
            plot_tool.main(config['folder'], result_df, config['scenario_sheet'])
        else:
            print('We prevented the plot GUI from popping up, since you are in '
                  'headless mode. To prevent this message from showing up again,'
                  ' please either remove the -p (plot) or -b (headless) from the'
                  ' simulation options')


if __name__ == "__main__":

    # default simulation parameters
    run_params = {'time_step': 0.03125,
                  'initial_time': 1995,
                  'final_time': 2050}

    # default configuration parameters
    config = {'model_name': '',
              'time': time.strftime('%H:%M'),
              'silent': False,
              'verbose': False,
              'headless': False,
              'extDataFname': '',
              'extDataFilePath': '',
              'return_timestep': 1.0,  # results will be stored every year
              'scenario_sheet': 'BAU',
              'plot': False,
              'run_params': run_params,
              'update_params': {},
              'fname': None}

    config = update_paths(config)

    # get command line parameters:
    config, run_params = get_initial_user_input(config, run_params)

    # loading the model object
    model = load_model(os.path.join(config['folder'], config['model_py']))

    # parameters to update (fow now empty)
    new_pars = {}

    # updating from World model used in EU model
    if config['geographical_level'] != 'global':
        config = create_external_data_files_paths(config)
        update_pars, config = load_external_data(config)
        update_pars = new_pars.update(update_pars)

    main(model, config, run_params, **new_pars)

