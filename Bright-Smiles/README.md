# Bright Smiles: Arizona acquisition screen

Screen of 3,000 fictional Arizona dental offices. The result is a shortlist of 50 pediatric practices worth a closer look for acquisition.

The Power BI report is one table joined to a map. The free license cannot publish a public link, so the recording is the click-through and the PDF is the still copy.

[Dashboard recording](report/live_report.mp4)

[Dashboard PDF](report/ONCAP.pdf)

The notebook is [analysis.ipynb](analysis.ipynb). City names come from [geocode_cities.py](geocode_cities.py). The dashboard table is [output/offices_enriched_with_rank.csv](output/offices_enriched_with_rank.csv).

## Conclusion

- 3,000 offices. **480** are pediatric.
- **Top 4** to avoid: Desert Valley Dental (294), Sunrise Family Dental (272), Arizona Smile Centers (248), Grand Canyon Dental (236). The next brand has 22 locations. These four own 157 pediatric offices.
- **157** other pediatric offices are in a city with trusted enrollment. Those were scored.
- Top office: Sunset Family Dental, Phoenix.
- Top 50 by city: Phoenix 29, Mesa 13, Gilbert 4, Chandler 2, Surprise 1, Tucson 1.
- Top 50 by brand: 43 brands. No brand has more than 2 offices.

## Data problems

- Population Mismatch: For 43 places in total **19** match Census population and were kept. **24** were set aside of our scoring system.
- Example: Sierra Vista is 3.0 million people in the file and about 45,000 in the Census.
- Sun, Sun CDP, Sun West, and Cocopah did not match one Census place. Those rows were dropped too.
- Office file has no city. A lookup from latitude and longitude left **651** offices with no city, including 106 pediatric offices outside the four major brands. They stay on the map and off the score.
- Some offices share the same name in the same city. But not row-level duplication.

## How the score works

Scored only if all three are true:

- Description contains pediatric, kids, children, or child. "Family" alone does not count.
- Brand is not one of the top 4.
- City is one of the 19 kept places:

$$
0.5 \leq \frac{\text{file population}}{\text{Census population}} \leq 2
$$

Among those 157 offices, $P(x)$ is the percentile of $x$ (0 to 1). Higher is better.

$$
\text{Child enrollment} = \text{preschool} + \text{kindergarten} + \text{grade 1} + \cdots + \text{grade 12}
$$

$$
\text{Kids per office} = \frac{\text{child enrollment}}{\text{pediatric offices in that city}}
$$

Major-brand pediatric offices are in the denominator. They are competitors, not targets.

- $v$ = this office's review count
- $R$ = this office's rating
- $1{,}862$ = median review count of the 157
- $3.73$ = average rating of the 157
- Weight on $R$ is $0.50$ only when $v = 1{,}862$. Fewer reviews put more weight on $3.73$.

$$
R_{\text{adjusted}} = \frac{v}{v + 1862} \cdot R + \frac{1862}{v + 1862} \cdot 3.73
$$

$$
\text{Score} = 0.25\, P(\text{child enrollment}) + 0.25\, P(\text{kids per office}) + 0.25\, P(R_{\text{adjusted}}) + 0.25\, P(\text{dentists})
$$

Top 50 = the 50 highest scores. Miles to the nearest other pediatric office are not in the score.

## Limitations and next steps

- Offices in the same city share one enrollment number. Inside Phoenix, rank is mostly rating and dentist count.
- The score does not include price, profit, willingness to sell, insurance mix, clinical outcomes, how full the schedule is, or the lease. Any of these can remove a name from the list.
- Distance is only the single nearest kids' office, not every competitor nearby.
- Equal weights are a choice. Income, population growth, and drive times were not added.