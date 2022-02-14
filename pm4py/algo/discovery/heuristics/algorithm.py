import pkgutil
from enum import Enum

from pm4py.algo.discovery.heuristics.variants import classic, plusplus
from pm4py.objects.conversion.log import converter as log_conversion
from pm4py.objects.heuristics_net.obj import HeuristicsNet
from pm4py.util import exec_utils
from typing import Optional, Dict, Any, Union, Tuple
from pm4py.objects.log.obj import EventLog, EventStream
import pandas as pd
from pm4py.objects.petri_net.obj import PetriNet, Marking


class Variants(Enum):
    CLASSIC = classic
    PLUSPLUS = plusplus


CLASSIC = Variants.CLASSIC
DEFAULT_VARIANT = CLASSIC

VERSIONS = {CLASSIC}


def apply(log: Union[EventLog, EventStream, pd.DataFrame], parameters: Optional[Dict[Any, Any]] = None, variant=CLASSIC) -> Tuple[PetriNet, Marking, Marking]:
    """
    Discovers a Petri net using Heuristics Miner

    Parameters
    ------------
    log
        Event log
    parameters
        Possible parameters of the algorithm,
        including:
            - Parameters.ACTIVITY_KEY
            - Parameters.TIMESTAMP_KEY
            - Parameters.CASE_ID_KEY
            - Parameters.DEPENDENCY_THRESH
            - Parameters.AND_MEASURE_THRESH
            - Parameters.MIN_ACT_COUNT
            - Parameters.MIN_DFG_OCCURRENCES
            - Parameters.DFG_PRE_CLEANING_NOISE_THRESH
            - Parameters.LOOP_LENGTH_TWO_THRESH
    variant
        Variant of the algorithm:
            - Variants.CLASSIC
            - Variants.PLUSPLUS

    Returns
    ------------
    net
        Petri net
    im
        Initial marking
    fm
        Final marking
    """
    if pkgutil.find_loader("pandas"):
        import pandas

        if isinstance(log, pandas.core.frame.DataFrame):
            return exec_utils.get_variant(variant).apply_pandas(log, parameters=parameters)

    return exec_utils.get_variant(variant).apply(log_conversion.apply(log, variant=log_conversion.Variants.TO_EVENT_LOG, parameters=parameters),
                                                 parameters=parameters)


def apply_dfg(dfg: Dict[Tuple[str, str], int], activities=None, activities_occurrences=None, start_activities=None, end_activities=None,
              parameters=None, variant=CLASSIC) -> Tuple[PetriNet, Marking, Marking]:
    """
    Discovers a Petri net using Heuristics Miner

    Parameters
    ------------
    dfg
        Directly-Follows Graph
    activities
        (If provided) list of activities of the log
    activities_occurrences
        (If provided) dictionary of activities occurrences
    start_activities
        (If provided) dictionary of start activities occurrences
    end_activities
        (If provided) dictionary of end activities occurrences
    parameters
        Possible parameters of the algorithm,
        including:
            - Parameters.ACTIVITY_KEY
            - Parameters.TIMESTAMP_KEY
            - Parameters.CASE_ID_KEY
            - Parameters.DEPENDENCY_THRESH
            - Parameters.AND_MEASURE_THRESH
            - Parameters.MIN_ACT_COUNT
            - Parameters.MIN_DFG_OCCURRENCES
            - Parameters.DFG_PRE_CLEANING_NOISE_THRESH
            - Parameters.LOOP_LENGTH_TWO_THRESH
    variant
        Variant of the algorithm:
            - Variants.CLASSIC

    Returns
    ------------
    net
        Petri net
    im
        Initial marking
    fm
        Final marking
    """
    return exec_utils.get_variant(variant).apply_dfg(dfg, activities=activities,
                                                     activities_occurrences=activities_occurrences,
                                                     start_activities=start_activities, end_activities=end_activities,
                                                     parameters=parameters)


def apply_heu(log: Union[EventLog, EventStream, pd.DataFrame], parameters: Optional[Dict[Any, Any]] = None, variant=CLASSIC) -> HeuristicsNet:
    """
    Discovers an Heuristics Net using Heuristics Miner

    Parameters
    ------------
    log
        Event log
    parameters
        Possible parameters of the algorithm,
        including:
            - Parameters.ACTIVITY_KEY
            - Parameters.TIMESTAMP_KEY
            - Parameters.CASE_ID_KEY
            - Parameters.DEPENDENCY_THRESH
            - Parameters.AND_MEASURE_THRESH
            - Parameters.MIN_ACT_COUNT
            - Parameters.MIN_DFG_OCCURRENCES
            - Parameters.DFG_PRE_CLEANING_NOISE_THRESH
            - Parameters.LOOP_LENGTH_TWO_THRESH
    variant
        Variant of the algorithm:
            - Variants.CLASSIC

    Returns
    ------------
    net
        Petri net
    im
        Initial marking
    fm
        Final marking
    """
    return exec_utils.get_variant(variant).apply_heu(log_conversion.apply(log, variant=log_conversion.Variants.TO_EVENT_LOG, parameters=parameters), parameters=parameters)


def apply_heu_dfg(dfg: Dict[Tuple[str, str], int], activities=None, activities_occurrences=None, start_activities=None, end_activities=None,
                  parameters=None, variant=CLASSIC) -> HeuristicsNet:
    """
    Discovers an Heuristics Net using Heuristics Miner

    Parameters
    ------------
    dfg
        Directly-Follows Graph
    activities
        (If provided) list of activities of the log
    activities_occurrences
        (If provided) dictionary of activities occurrences
    start_activities
        (If provided) dictionary of start activities occurrences
    end_activities
        (If provided) dictionary of end activities occurrences
    parameters
        Possible parameters of the algorithm,
        including:
            - Parameters.ACTIVITY_KEY
            - Parameters.TIMESTAMP_KEY
            - Parameters.CASE_ID_KEY
            - Parameters.DEPENDENCY_THRESH
            - Parameters.AND_MEASURE_THRESH
            - Parameters.MIN_ACT_COUNT
            - Parameters.MIN_DFG_OCCURRENCES
            - Parameters.DFG_PRE_CLEANING_NOISE_THRESH
            - Parameters.LOOP_LENGTH_TWO_THRESH
    variant
        Variant of the algorithm:
            - Variants.CLASSIC

    Returns
    ------------
    net
        Petri net
    im
        Initial marking
    fm
        Final marking
    """
    return exec_utils.get_variant(variant).apply_heu_dfg(dfg, activities=activities,
                                                         activities_occurrences=activities_occurrences,
                                                         start_activities=start_activities,
                                                         end_activities=end_activities,
                                                         parameters=parameters)
