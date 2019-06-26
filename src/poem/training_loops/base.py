# -*- coding: utf-8 -*-

"""Training loops for KGE models using multi-modal information."""

import logging
from abc import ABC, abstractmethod
from typing import List, Tuple

import numpy as np
import torch
import torch.nn as nn

from ..instance_creation_factories.instances import Instances

__all__ = [
    'TrainingLoop',
]

log = logging.getLogger(__name__)


class TrainingLoop(ABC):
    def __init__(
            self,
            kge_model: nn.Module,
            optimizer: torch.optim.Optimizer,
            all_entities: np.ndarray = None,
    ) -> None:
        self.kge_model = kge_model
        self.optimizer = optimizer
        self.losses_per_epochs = []
        self.all_entities = all_entities

    @property
    def device(self):
        return self.kge_model.device

    @abstractmethod
    def train(
            self,
            training_instances: Instances,
            num_epochs,
            batch_size,
    ) -> Tuple[nn.Module, List[float]]:
        """Train the KGE model.

        :return: A pair of the KGE model and the losses per epoch.
        """
