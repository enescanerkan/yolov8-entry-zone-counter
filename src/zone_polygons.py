"""
Author: Enes Can Erkan
Date: 2024-06-28
"""

import numpy as np


def get_human_zone_polygon():
    """
    İnsanlar için ZONE_POLYGON koordinatlarını döndürür.

    :return: HUMAN_ZONE_POLYGON koordinatları
    """
    return np.array([
        [0.74, 0.35],  # Sol üst köşe
        [0.76, 0.35],  # Sağ üst köşe
        [0.7, 1],      # Sağ alt köşe
        [0.5, 1]       # Sol alt köşe
    ])
