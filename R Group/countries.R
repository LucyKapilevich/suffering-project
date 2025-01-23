library('tidyverse')
library('ggplot2')

custom_palette <- c(
  "#1F77B4", # Blue
  "#FF7F0E", # Orange
  "#2CA02C", # Green
  "#D62728", # Red
  "#9467BD", # Purple
  "#8C564B", # Brown
  "#E377C2", # Pink
  "#7F7F7F", # Gray
  "#BCBD22", # Yellow-green
  "#17BECF"  # Cyan
)

# Load and preprocess the data
hidata <- read_csv('history_data.csv') |> 
  rename(
    'Birthyear' = 'Birth Year',
    'Deathyear' = 'Death Year',
    'Birthplace' = 'Birth Place',
    'Deathcause' = 'Death Cause',
    'Awardnumber' = 'Award Number',
    'Spousenumber' = 'Spouse Number'
  )

# Calculate Lifespan and filter invalid values
spandata <- hidata |>
  mutate(Lifespan = Deathyear - Birthyear) |> 
  filter(Lifespan <= 123 & Lifespan >= 0) |>
  filter(Birthyear <= 1950 & Birthyear >= 1750) |>  
  filter(!is.na(Birthplace) & !is.na(Birthyear)) |> print()  

# Group data by Birth year and Birthplace to calculate average lifespan per year and country
threshold <- 30
yearly_data <- spandata |> 
  mutate(decade = floor(Birthyear / 10) * 10) |>
  group_by(Birthplace) |>
  filter(n()>= threshold) |>
  group_by(Birthplace, decade) |>
  summarise(mean_lifespan = mean(Lifespan, na.rm = TRUE)) |>
  print()
#check <- distinct(yearly_data, Birthplace)
            
#count = n()) |>
#filter(count >= 20)

# Filter specific countries 
selected_countries <- c("Australia","United States","Russia","United Kingdom","China","Brazil", "South Africa", "Algeria", "Pakistan", "Egypt")
filtered_yearly_data <- yearly_data |>
  filter(Birthplace %in% selected_countries)

ggplot(data = filtered_yearly_data) +
  aes(x = decade, y = mean_lifespan, color = Birthplace, group = Birthplace) +
  geom_line(size = 0.5, alpha = 0.8) +
  scale_color_manual(values = custom_palette) + # Use the custom palette
  labs(
    x = "Decade of birth (10 years)",
    y = "Average Lifespan (years)",
    #title = "Average Lifespan Over Time by Country",
    color = "Country"
  ) +
  theme_bw() +
  theme(
    legend.position = "right"  
  )

ggsave('countrylife.pdf')




