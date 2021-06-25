from enum import Enum
from typing import Dict, Optional, Any

import pandas as pd

from pm4py.statistics.traces.cycle_time.util import compute
from pm4py.util import exec_utils, constants, xes_constants


class Parameters(Enum):
    TIMESTAMP_KEY = constants.PARAMETER_CONSTANT_TIMESTAMP_KEY
    START_TIMESTAMP_KEY = constants.PARAMETER_CONSTANT_START_TIMESTAMP_KEY
    CASE_ID_KEY = constants.PARAMETER_CONSTANT_CASEID_KEY


def apply(df: pd.DataFrame, parameters: Optional[Dict[str, Any]] = None) -> float:
    """
    Computes the cycle time starting from a Pandas dataframe

    The definition that has been followed is the one proposed in:
    https://www.presentationeze.com/presentations/lean-manufacturing-just-in-time/lean-manufacturing-just-in-time-full-details/process-cycle-time-analysis/calculate-cycle-time/#:~:text=Cycle%20time%20%3D%20Average%20time%20between,is%2024%20minutes%20on%20average.

    So:
    Cycle time  = Average time between completion of units.

    Example taken from the website:
    Consider a manufacturing facility, which is producing 100 units of product per 40 hour week.
    The average throughput rate is 1 unit per 0.4 hours, which is one unit every 24 minutes.
    Therefore the cycle time is 24 minutes on average.
    
    Parameters
    ------------------
    df
        Dataframe
    parameters
        Parameters of the algorithm, including:
        - Parameters.START_TIMESTAMP_KEY => the attribute acting as start timestamp
        - Parameters.TIMESTAMP_KEY => the attribute acting as timestamp
        - Parameters.CASE_ID_KEY => the attribute acting as case identifier

    Returns
    ------------------
    cycle_time
        Cycle time
    """
    if parameters is None:
        parameters = {}

    start_timestamp_key = exec_utils.get_param_value(Parameters.START_TIMESTAMP_KEY, parameters,
                                                     xes_constants.DEFAULT_TIMESTAMP_KEY)
    timestamp_key = exec_utils.get_param_value(Parameters.TIMESTAMP_KEY, parameters,
                                               xes_constants.DEFAULT_TIMESTAMP_KEY)
    case_id_key = exec_utils.get_param_value(Parameters.CASE_ID_KEY, parameters, constants.CASE_CONCEPT_NAME)

    events = [(x[start_timestamp_key].timestamp(), x[timestamp_key].timestamp()) for x in
              df[{start_timestamp_key, timestamp_key}].to_dict("r")]

    return compute.cycle_time(events, df[case_id_key].nunique())
