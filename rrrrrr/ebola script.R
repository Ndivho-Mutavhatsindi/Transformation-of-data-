print(linelist_cleaned)
install.packages("rio")
table()
library(rio)
library(tidyverse)
# import your dataset
linelist <- import("linelist_cleaned.rds")

linelist <- linelist %>% 
  mutate(delay_cat = case_when(
    # criteria                                   # new value if TRUE
    days_onset_hosp < 2                        ~ "<2 days",
    days_onset_hosp >= 2 & days_onset_hosp < 5 ~ "2-5 days",
    days_onset_hosp >= 5                       ~ ">5 days",
    is.na(days_onset_hosp)                     ~ NA_character_,
    TRUE                                       ~ "Check me"))  

table(linelist$delay_cat, useNA = "always")

linelist <- linelist %>%
  mutate(delay_cat = fct_relevel(delay_cat))

levels(linelist$delay_cat)

linelist <- linelist %>%
  mutate(delay_cat = fct_relevel(delay_cat, "<2 days", "2-5 days", ">5 days"))

ggplot(data = linelist)+
  geom_bar(mapping = aes(x = delay_cat))

install.packages("janitor")
library(janitor)

linelist %>% 
  mutate(delay_cat = fct_expand(delay_cat, "Not admitted to hospital", "Transfer to other jurisdiction")) %>% 
  tabyl(delay_cat)   # print table

linelist %>% 
  mutate(delay_cat = fct_drop(delay_cat)) %>% 
  tabyl(delay_cat)


