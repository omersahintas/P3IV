
import numpy as np
from copy import deepcopy
from p3iv_modules.interfaces.action import ActInterface


class Act(object):
    def __call__(self, motion_plans):
        """
        # NOTE THAT,
        # with timeshifting planner, combinatorial aspect in its classical sense is abandoned.
        """

        best_index = self.determine_the_optimal_motion_plan(motion_plans)
        # deepcopy to allow modifications later on
        mp = deepcopy(motion_plans[best_index])
        return mp

    @staticmethod
    def determine_the_optimal_motion_plan(motion_plans):
        lowest_cost = min([mp.cost for mp in motion_plans if mp.motion is not None])
        best_index = [
            i
            for i in range(len(motion_plans))
            if motion_plans[i].motion is not None
            and motion_plans[i].cost == lowest_cost
        ][0]
        return best_index
