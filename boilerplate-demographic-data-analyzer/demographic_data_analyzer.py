import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count  = df['race'].value_counts() 
    race_count

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)
    average_age_men

    # What is the percentage of people who have a Bachelor's degree?
    #count the total numbers of entries in the dataset
    total_count = len(df)
    #Counting how many of those entries have "Bachelors" in the education column.
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors =round((bachelors_count / total_count) * 100, 1)
    percentage_bachelors
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # Define advanced education levels
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    # Filter the data for those without advanced education
    lower_education = df[~df['education'].isin(advanced_education)]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1)
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #Filter the dataset for individuals who work the minimum number of hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    min_workers
    
    # Percentage of those people who earn >50K
    if len(min_workers) > 0:
        rich_percentage = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / len(min_workers)) * 100, 1)
    else:
        rich_percentage = 0

    # Country with highest percentage of rich
    countries = df['native-country'].unique()
    rich_percentage_by_country = {}

    for country in countries:
        country_df = df[df['native-country'] == country]
        if len(country_df) > 0:
            rich_percentage_country = round((country_df[country_df['salary'] == '>50K'].shape[0] / country_df.shape[0]) * 100, 1)
            rich_percentage_by_country[country] = rich_percentage_country

    highest_earning_country = max(rich_percentage_by_country, key=rich_percentage_by_country.get)
    highest_earning_country_percentage = rich_percentage_by_country[highest_earning_country]


    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    india_high_earners
    top_IN_occupation = india_high_earners['occupation'].mode()[0]
    top_IN_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
