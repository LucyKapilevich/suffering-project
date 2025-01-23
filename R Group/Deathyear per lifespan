library('tidyverse')
library('ggplot2')
library('dplyr')

hidata <- read_csv('history_data.csv') |> rename('Birthyear' = 'Birth Year', 'Deathyear' = 'Death Year', 
                                                 'Birthplace'='Birth Place', 'Deathcause' ='Death Cause', 
                                                 'Awardnumber'= 'Award Number', 'Spousenumber'='Spouse Number')
spandata <- mutate(hidata, Lifespan = Deathyear - Birthyear) |> filter(Lifespan <=123 & Lifespan >= 0) |> 
  filter(Birthyear <= 1950 & Birthyear >= 0) |> print()

bidata <- group_by(spandata, Deathyear) |> summarise(mlife = mean(Lifespan))

ggplot(data=bidata) +
  aes(x = Deathyear, y= mlife)+
  geom_smooth()+
  labs(
    x = 'Year of Death',
    y = 'Lifespan' ,
  )



ggsave('deathyear_lifespan.pdf')
