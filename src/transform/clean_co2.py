import pandas as pd


def drop_unnecessary_columns(df_co2):
    # Drop unnecessary columns from the CO2 DataFrame
    df_co2.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
    return df_co2


def drop_records_outside_timeline(df_co2):
    # Drop records outside the desired timeline
    df_co2 = df_co2[df_co2['year'].between(1994, 2023)].reset_index(drop=True)
    return df_co2


def drop_records_with_missing_values(df_co2):
    # Drop records with missing values in the CO2 DataFrame
    # iso_code 0 indicates aggregate country i.e. Global/Africa
    df_co2 = df_co2[df_co2['iso_code'] != 0]
    # Drop countries with zero population
    df_co2 = df_co2[
        ~df_co2['country'].isin(['Antarctica', 'Christmas Island'])
    ]
    # Drop countries with zero GDP for all records
    zero_counts = df_co2[df_co2['gdp'] == 0.0].groupby('country').size()
    df_co2 = df_co2[
        ~df_co2['country'].isin(zero_counts[zero_counts == 30].index)
    ]
    return df_co2


def calculate_missing_values(df_co2):
    # Fill missing GDP values with the mean GDP of each country
    mean_gdp = df_co2[df_co2['gdp'] != 0.0].groupby('country')['gdp'].mean()
    df_co2.loc[df_co2['gdp'] == 0.0, 'gdp'] = df_co2['country'].map(mean_gdp)
    return df_co2


def drop_null_columns(df_co2):
    # Function to determine 0.0 values as percentage of total values
    # in each column
    def count_zeros(df):
        return (df == 0).mean() * 100
    # Store columns with no null values
    nulls_co2 = pd.Series(count_zeros(df_co2))
    df_co2 = df_co2[nulls_co2[nulls_co2 == 0].index].reset_index(drop=True)
    return df_co2


def convert_columns_types(df_co2):
    # Convert columns to appropriate data types
    df_co2['population'] = df_co2['population'].astype(int)
    df_co2['gdp'] = df_co2['gdp'].astype(int)
    return df_co2


def enrich_data(df_co2):
    # Add additional column that will check the country and select a suitable
    # region for association
    # Define region mapping for all 255 countries in the current dataframe
    region_map = {
        # Africa
        'Algeria': 'Africa',
        'Angola': 'Africa',
        'Benin': 'Africa',
        'Botswana': 'Africa',
        'Burkina Faso': 'Africa',
        'Burundi': 'Africa',
        'Cabo Verde': 'Africa',
        'Cameroon': 'Africa',
        'Central African Republic': 'Africa',
        'Chad': 'Africa',
        'Comoros': 'Africa',
        'Congo': 'Africa',
        'Democratic Republic of Congo': 'Africa',
        'Djibouti': 'Africa',
        'Egypt': 'Africa',
        'Equatorial Guinea': 'Africa',
        'Eritrea': 'Africa',
        'Eswatini': 'Africa',
        'Ethiopia': 'Africa',
        'Gabon': 'Africa',
        'Gambia': 'Africa',
        'Ghana': 'Africa',
        'Guinea': 'Africa',
        'Guinea-Bissau': 'Africa',
        'Ivory Coast': 'Africa',
        "Cote d'Ivoire": 'Africa',
        'Kenya': 'Africa',
        'Lesotho': 'Africa',
        'Liberia': 'Africa',
        'Libya': 'Africa',
        'Madagascar': 'Africa',
        'Malawi': 'Africa',
        'Mali': 'Africa',
        'Mauritania': 'Africa',
        'Mauritius': 'Africa',
        'Morocco': 'Africa',
        'Mozambique': 'Africa',
        'Namibia': 'Africa',
        'Niger': 'Africa',
        'Nigeria': 'Africa',
        'Rwanda': 'Africa',
        'Sao Tome and Principe': 'Africa',
        'Senegal': 'Africa',
        'Seychelles': 'Africa',
        'Sierra Leone': 'Africa',
        'Somalia': 'Africa',
        'South Africa': 'Africa',
        'South Sudan': 'Africa',
        'Sudan': 'Africa',
        'Tanzania': 'Africa',
        'Togo': 'Africa',
        'Tunisia': 'Africa',
        'Uganda': 'Africa',
        'Zambia': 'Africa',
        'Zimbabwe': 'Africa',
        'Liberia': 'Africa',
        'Libya': 'Africa',
        'Madagascar': 'Africa',
        'Malawi': 'Africa',
        'Mali': 'Africa',
        'Mauritania': 'Africa',
        'Mauritius': 'Africa',
        'Morocco': 'Africa',
        'Mozambique': 'Africa',
        'Namibia': 'Africa',
        'Niger': 'Africa',
        'Nigeria': 'Africa',
        'Rwanda': 'Africa',
        'Sao Tome and Principe': 'Africa',
        'Senegal': 'Africa',
        'Seychelles': 'Africa',
        'Sierra Leone': 'Africa',
        'Somalia': 'Africa',
        'South Africa': 'Africa',
        'South Sudan': 'Africa',
        'Sudan': 'Africa',
        'Tanzania': 'Africa',
        'Togo': 'Africa',
        'Tunisia': 'Africa',
        'Uganda': 'Africa',
        'Zambia': 'Africa',
        'Zimbabwe': 'Africa',

        # Asia
        'Afghanistan': 'Asia',
        'Armenia': 'Asia',
        'Azerbaijan': 'Asia',
        'Bahrain': 'Asia',
        'Bangladesh': 'Asia',
        'Bhutan': 'Asia',
        'Brunei': 'Asia',
        'Cambodia': 'Asia',
        'China': 'Asia',
        'Cyprus': 'Asia',
        'Georgia': 'Asia',
        'India': 'Asia',
        'Indonesia': 'Asia',
        'Iran': 'Asia',
        'Iraq': 'Asia',
        'Israel': 'Asia',
        'Japan': 'Asia',
        'Jordan': 'Asia',
        'Kazakhstan': 'Asia',
        'Kuwait': 'Asia',
        'Kyrgyzstan': 'Asia',
        'Laos': 'Asia',
        'Lebanon': 'Asia',
        'Malaysia': 'Asia',
        'Maldives': 'Asia',
        'Mongolia': 'Asia',
        'Myanmar': 'Asia',
        'Nepal': 'Asia',
        'North Korea': 'Asia',
        'Oman': 'Asia',
        'Pakistan': 'Asia',
        'Palestine': 'Asia',
        'Philippines': 'Asia',
        'Qatar': 'Asia',
        'Saudi Arabia': 'Asia',
        'Singapore': 'Asia',
        'South Korea': 'Asia',
        'Sri Lanka': 'Asia',
        'Syria': 'Asia',
        'Taiwan': 'Asia',
        'Tajikistan': 'Asia',
        'Thailand': 'Asia',
        'Timor': 'Asia',
        'East Timor': 'Asia',
        'Turkey': 'Asia',
        'Turkmenistan': 'Asia',
        'United Arab Emirates': 'Asia',
        'Uzbekistan': 'Asia',
        'Vietnam': 'Asia',
        'Yemen': 'Asia',

        # Europe
        'Albania': 'Europe',
        'Andorra': 'Europe',
        'Austria': 'Europe',
        'Belarus': 'Europe',
        'Belgium': 'Europe',
        'Bosnia and Herzegovina': 'Europe',
        'Bulgaria': 'Europe',
        'Croatia': 'Europe',
        'Czechia': 'Europe',
        'Denmark': 'Europe',
        'Estonia': 'Europe',
        'Finland': 'Europe',
        'France': 'Europe',
        'Germany': 'Europe',
        'Greece': 'Europe',
        'Hungary': 'Europe',
        'Iceland': 'Europe',
        'Ireland': 'Europe',
        'Italy': 'Europe',
        'Kosovo': 'Europe',
        'Latvia': 'Europe',
        'Liechtenstein': 'Europe',
        'Lithuania': 'Europe',
        'Luxembourg': 'Europe',
        'Malta': 'Europe',
        'Moldova': 'Europe',
        'Monaco': 'Europe',
        'Montenegro': 'Europe',
        'Netherlands': 'Europe',
        'North Macedonia': 'Europe',
        'Norway': 'Europe',
        'Poland': 'Europe',
        'Portugal': 'Europe',
        'Romania': 'Europe',
        'Russia': 'Europe',
        'San Marino': 'Europe',
        'Serbia': 'Europe',
        'Slovakia': 'Europe',
        'Slovenia': 'Europe',
        'Spain': 'Europe',
        'Sweden': 'Europe',
        'Switzerland': 'Europe',
        'Ukraine': 'Europe',
        'United Kingdom': 'Europe',
        'Vatican': 'Europe',

        # North America
        'Antigua and Barbuda': 'North America',
        'Bahamas': 'North America',
        'Barbados': 'North America',
        'Belize': 'North America',
        'Canada': 'North America',
        'Costa Rica': 'North America',
        'Cuba': 'North America',
        'Dominica': 'North America',
        'Dominican Republic': 'North America',
        'El Salvador': 'North America',
        'Grenada': 'North America',
        'Guatemala': 'North America',
        'Haiti': 'North America',
        'Honduras': 'North America',
        'Jamaica': 'North America',
        'Mexico': 'North America',
        'Nicaragua': 'North America',
        'Panama': 'North America',
        'Saint Kitts and Nevis': 'North America',
        'Saint Lucia': 'North America',
        'Saint Vincent and the Grenadines': 'North America',
        'Trinidad and Tobago': 'North America',
        'United States': 'North America',

        # South America
        'Argentina': 'South America',
        'Bolivia': 'South America',
        'Brazil': 'South America',
        'Chile': 'South America',
        'Colombia': 'South America',
        'Ecuador': 'South America',
        'Guyana': 'South America',
        'Paraguay': 'South America',
        'Peru': 'South America',
        'Suriname': 'South America',
        'Uruguay': 'South America',
        'Venezuela': 'South America',

        # Oceania
        'Australia': 'Oceania',
        'Fiji': 'Oceania',
        'Kiribati': 'Oceania',
        'Marshall Islands': 'Oceania',
        'Micronesia (country)': 'Oceania',
        'Nauru': 'Oceania',
        'New Zealand': 'Oceania',
        'Palau': 'Oceania',
        'Papua New Guinea': 'Oceania',
        'Samoa': 'Oceania',
        'Solomon Islands': 'Oceania',
        'Tonga': 'Oceania',
        'Tuvalu': 'Oceania',
        'Vanuatu': 'Oceania',

        # Other/Unclassified
        'Hong Kong': 'Other',
        'Macao': 'Other',
        'Greenland': 'Other',
        'Bermuda': 'Other',
        'Aruba': 'Other',
        'Curaçao': 'Other',
        'Sint Maarten (Dutch part)': 'Other',
        'Bonaire Sint Eustatius and Saba': 'Other',
        'Montserrat': 'Other',
        'Anguilla': 'Other',
        'British Virgin Islands': 'Other',
        'Cayman Islands': 'Other',
        'Falkland Islands': 'Other',
        'French Polynesia': 'Other',
        'Gibraltar': 'Other',
        'Guadeloupe': 'Other',
        'Martinique': 'Other',
        'Mayotte': 'Other',
        'New Caledonia': 'Other',
        'Niue': 'Other',
        'Réunion': 'Other',
        'Saint Helena': 'Other',
        'Saint Pierre and Miquelon': 'Other',
        'Turks and Caicos Islands': 'Other',
        'Wallis and Futuna': 'Other',
        'Faroe Islands': 'Other',
        'Saint Barthélemy': 'Other',
        'Saint Martin (French part)': 'Other',
        'Ryukyu Islands': 'Other',
        'Ryukyu Islands (GCP)': 'Other',
        'Kuwaiti Oil Fires': 'Other',
        'Kuwaiti Oil Fires (GCP)': 'Other',
        'Christmas Island': 'Other'
    }

    def assign_region(country):
        return region_map.get(country, 'Other')

    df_co2['region'] = df_co2['country'].apply(assign_region)
    return df_co2


def clean_co2(df_co2):
    df_co2 = drop_unnecessary_columns(df_co2)
    df_co2 = drop_records_outside_timeline(df_co2)
    df_co2 = drop_records_with_missing_values(df_co2)
    df_co2 = calculate_missing_values(df_co2)
    df_co2 = drop_null_columns(df_co2)
    df_co2 = convert_columns_types(df_co2)
    df_co2 = enrich_data(df_co2)
    return df_co2
