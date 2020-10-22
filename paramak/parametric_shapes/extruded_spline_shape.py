from collections import Iterable

import cadquery as cq

from paramak import ExtrudeMixedShape


class ExtrudeSplineShape(ExtrudeMixedShape):
    """Extrudes a 3d CadQuery solid from points connected with spline
    connections.

    Args:
        points (list): list of (float, float) containing each point
            coordinates.
        distance (float): the extrusion distance to use (cm units if used for
            neutronics)
        stp_filename (str, optional): Defaults to "ExtrudeSplineShape.stp".
        stl_filename (str, optional): Defaults to "ExtrudeSplineShape.stl".
    """

    def __init__(
        self,
        points,
        distance,
        stp_filename="ExtrudeSplineShape.stp",
        stl_filename="ExtrudeSplineShape.stl",
        **kwargs
    ):

        super().__init__(
            points=[(*p, "spline") for p in points],
            distance=distance,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )
