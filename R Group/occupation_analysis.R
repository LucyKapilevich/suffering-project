library('tidyverse')
library('ggplot2')
library('dplyr')

occdata <- read_csv('occupation_data.csv')

# Calculate the row-wise mean lifespan
occdata <- occdata |>
  mutate(avg_lifespan = rowMeans(select(occdata, starts_with("Lifespan_")), na.rm = TRUE)) |>
  select(-starts_with("Lifespan_")) |>
  rename('averageLifespan' = 'avg_lifespan') |>
  mutate(Occupation = fct_reorder(Occupation, averageLifespan, .desc=TRUE))

ggplot(data = occdata) +
  aes(x = Occupation, y = averageLifespan, fill = averageLifespan) +
  theme_bw() +
  theme(axis.title.x = element_blank())+
  geom_col() +
  coord_flip() +
  geom_vline(xintercept = 70.2) + # comment do your own average
  labs(
    x = 'Occupation',
    y = 'Average lifespan per occupation (years)',
    fill = 'Average Lifespan'
  )+
  theme(axis.text.x = element_text(vjust = 0.5, hjust = 0.5))

