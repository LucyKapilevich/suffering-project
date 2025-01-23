library('tidyverse')
library('ggplot2')
library('dplyr')

reldata <- read_csv('religion_data.csv')

# Calculate the row-wise mean lifespan
reldata <- reldata |>
  
  mutate(avg_lifespan = rowMeans(select(reldata, starts_with("Lifespan_")), na.rm = TRUE)) |>
  select(-starts_with("Lifespan_")) |>
  rename('averageLifespan' = 'avg_lifespan')

reldata <- reldata |> 
  mutate(Religion = fct_reorder(Occupation, averageLifespan, .desc=TRUE))

ggplot(data = reldata) +
  aes(x = Religion, y = averageLifespan, fill = averageLifespan) +
  theme_bw() +
  theme(axis.title.x = element_blank())+
  geom_col() +
  geom_vline(xintercept = 70.2) + # comment do your own average
  labs(
    x = 'Religion',
    y = 'Average lifespan per occupation (years)',
    fill = 'Average lifespan'
  )+
  theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust = 0.5))
