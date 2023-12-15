import xarray as xr


@xr.register_dataset_accessor("eda")
class GeoAccessor:
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def plot(self, col_wrap=5, vmax=0.2, **kwargs):
        if isinstance(self._obj, xr.Dataset):
            self._obj[
                kwargs.get("variables", ["red", "green", "blue"])
            ].to_array(dim="band").plot.imshow(
                col="time", col_wrap=col_wrap, vmax=vmax, **kwargs
            )

    def plot_index(self):
        self._obj.plot.imshow(y="time")
