import xarray as xr
import os
os.chdir("/mnt/d/BR-DWG/pr_Tmax_Tmin_NetCDF_Files/")
file_list = [
  "pr_19610101_19801231_BR-DWGD_UFES_UTEXAS_v_3.2.2.nc", "pr_19810101_20001231_BR-DWGD_UFES_UTEXAS_v_3.2.2.nc",
  "pr_20010101_20200731_BR-DWGD_UFES_UTEXAS_v_3.2.2.nc", "pr_20200801_20221231_BR-DWGD_UFES_UTEXAS_v_3.2.2.nc"
]

for file in file_list:
    ds = xr.open_dataset(file)
    # 2. Calculate the 50-day rolling sum
    ds_rolling = ds['pr'].rolling(time=50, min_periods=50).sum()
    
    # 3. Resample the data annually and calculate the maximum 50-day sum for each year
    n50days = ds_rolling.resample(time='1Y').max(dim='time')
    
    # 4. Optionally, assign the result to a new dataset
    ds_n50days = n50days.to_dataset(name='N50Days')
    

