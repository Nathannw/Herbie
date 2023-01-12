# What is Herbie?

Herbie is a package that gives you access to archived and real-time numerical weather prediction model data.

- Discover if data you want exists and where it exists.
- Show the file contents (file inventory).
- Download the file to your local computer.
- Open data in xarray.
- Provide some helpers to work with the data in xarray.

Access data from multiple sources. You shouldn't  need toworry *where* the data lives. Herbie will look at different data sources for the data you need. For example, if the data is on AWS, then get the data from there, but if the file is missing, then Herbie will check see if the data is on NOMADS or GCP, etc.

Herbie can download a file to your computer. Once you have the file, you can open it with xarray.


**What is Herbie good for?**
Herbie is great if you don't need to consume a huge amount of data. What is a huge amount? I wo't tell you what the "ideal" limit is.
 
> Note: If you need to download "lots" of full files, then I'd recomend using another tool like rclone. You can still use Herbie to discover the local files (provided the files are in the local location Herbie expects.)


**What data can Herbie download?**
Herbie is currently designed to access GRIB2 data, a format that virtually all numerical weather prediction is distributed. 


**Is GRIB2 Cloud Optimized?**
Many would say GRIB2 is not "cloud-optimized", but, if you are interested in the whole model grid, then GRIB is cloud-optimized. With Herbie, you can download a subset of a file by variable (more specifically, GRIB message), provided an inventory of the file contents and byte range exists.


**Why is it named Herbie?**
- Herbie was originally nammed "hrrrb", because it only managed HRRR model data, and the "b" is from my name (Brian). Herbie was later expanded to work with lots of different types of models, and I needed a name that was more general than just one model. That is when Herbie was born. No offense to any other packages, but I am not a fan of using acronyms to name things. I actually love the name Herbie because it gives the package some personality. In fact, Herbie is named after one of my favorite childhood movies about a small racecar that is full personality. 


