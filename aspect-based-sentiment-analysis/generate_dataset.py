import csv

turnover = open('lovemondays_turnover.csv', 'w+', encoding='utf8')

csv_writer = csv.writer(turnover, delimiter=',', lineterminator='\n')

def create_columns():
    csv_writer.writerow(["pay", "conditions", "nature_of_work", "promotion", "supervision", "rewards", "coworkers", "communication", "benefits", "former_emp"])

def generate_quantitative_dataset(sentiment, aspect):
    if (aspect == 'pay'):
        csv_writer.writerow([sentiment, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    if (aspect == 'conditions'):
        csv_writer.writerow([0, sentiment, 0, 0, 0, 0, 0, 0, 0, 1])
    if (aspect == 'nature_of_work'):
        csv_writer.writerow([0, 0, sentiment, 0, 0, 0, 0, 0, 0, 1])
    if (aspect == 'promotion'):
        csv_writer.writerow([0, 0, 0, sentiment, 0, 0, 0, 0, 0, 1])
    if (aspect == 'supervision'):
        csv_writer.writerow([0, 0, 0, 0, sentiment, 0, 0, 0, 0, 1])
    if (aspect == 'rewards'):
        csv_writer.writerow([0, 0, 0, 0, 0, sentiment, 0, 0, 0, 1])
    if (aspect == 'coworkers'):
        csv_writer.writerow([0, 0, 0, 0, 0, 0, sentiment, 0, 0, 1])
    if (aspect == 'communication'):
        csv_writer.writerow([0, 0, 0, 0, 0, 0, 0, sentiment, 0, 1])
    if (aspect == 'benefits'):
        csv_writer.writerow([0, 0, 0, 0, 0, 0, 0, 0, sentiment, 1])