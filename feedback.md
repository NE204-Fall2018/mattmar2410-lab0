# Overall (87/100)
 - The inclusion of the abstract is a nice touch

# Build (10/10)
 - Nice addition of `requirements.txt` for handling dependencies: might also
   be good to include your python version (also, you missed the `statsmodels`
   dependency)
 - Good modification of the README to describe your project and build 
   build procedure

# Testing (10/10)
 - In general, don't need to test the tools in the module (numpy has its
   own test suite that I'm sure includes tests for polyfit) - want your
   designed tests to focus on the things unique to your implementations

# Introduction / Motivation / Background (15/15)
 - Adequate level of background for lab 0. For future labs, be sure to 
   emphasize the what and the why in the introduction.

# Methods (13/15)
 - Adequate description of the specific process, particularly with respect to
   peak-finding. Other subtasks such as centroid determination (e.g. from 
   peak-fitting) could use a deeper explanation.

# Results and Discussion (32/40)
 - Presentation of results seems "backwards" - information about calibration 
   validation is presented before the energy calibration results themselves
 - Careful with sig-figs: your eqn. 1 implies sub-eV precision in the results
   of your calibration, which are not supported by the nuclear data (and 
   probably not justified by the centroid determination method, though these
   results are absent)
 - Figures are appropriately labeled/titled/captioned
 - Though there are quantitative values for uncertainties listed, there is no
   discussion as to where they came from (see comments.pdf). You should always
   explain how the uncertainties arise and where they come from, especially in
   the case of derived uncertainties

# Conclusion (7/10)
 - Though you don't need an explicit conclusion section, more focus on the
   quantitative results and a discussion of what was learned and any 
   limitations related to the presented approach are warranted.
