import numpy as np
from eemeter.caltrack.daily.utilities.utils import ModelCoefficients, ModelType
from eemeter.caltrack.daily.utilities.config import DailySettings as Settings
from eemeter.caltrack.daily.base_models.c_hdd_tidd import fit_c_hdd_tidd
from eemeter.caltrack.daily.fit_base_models import _get_opt_options


def test_fit_c_hdd_tidd_smooth():
    # Test case 1: Test with initial_fit=True
    T = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).astype(float)
    obs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).astype(float)
    settings = Settings(
        developer_mode=True,
        alpha_selection=0.1,
        alpha_final=0.2,
        segment_minimum_count=5,
        maximum_slope_OoM_scaler=1,
    )
    opt_options = _get_opt_options(settings)
    x0 = ModelCoefficients(
        model_type=ModelType.HDD_TIDD_SMOOTH,
        intercept=0.0,
        hdd_bp=0.0,
        hdd_beta=0.0,
        hdd_k=0.0,
        cdd_bp=None,
        cdd_beta=None,
        cdd_k=None,
    )
    bnds = None
    initial_fit = True
    smooth = True
    res = fit_c_hdd_tidd(T, obs, settings, opt_options, smooth, x0, bnds, initial_fit)
    assert res.success == True

    # Test case 2: Test with initial_fit=False
    T = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).astype(float)
    obs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).astype(float)
    settings = Settings(
        developer_mode=True,
        alpha_selection=0.1,
        alpha_final=0.2,
        segment_minimum_count=5,
        maximum_slope_OoM_scaler=1,
    )
    opt_options = _get_opt_options(settings)
    x0 = ModelCoefficients(
        model_type=ModelType.HDD_TIDD_SMOOTH,
        intercept=0.0,
        hdd_bp=0.0,
        hdd_beta=0.0,
        hdd_k=0.0,
        cdd_bp=None,
        cdd_beta=None,
        cdd_k=None,
    )
    bnds = None
    initial_fit = False
    smooth = True
    res = fit_c_hdd_tidd(T, obs, settings, opt_options, smooth, x0, bnds, initial_fit)
    assert res.success == True

    # Test case 3: Test with x0=None
    T = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).astype(float)
    obs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).astype(float)
    settings = Settings(
        developer_mode=True,
        alpha_selection=0.1,
        alpha_final=0.2,
        segment_minimum_count=5,
        maximum_slope_OoM_scaler=1,
    )
    opt_options = _get_opt_options(settings)
    x0 = None
    bnds = None
    initial_fit = True
    smooth = True
    res = fit_c_hdd_tidd(T, obs, settings, opt_options, smooth, x0, bnds, initial_fit)
    assert res.success == True
