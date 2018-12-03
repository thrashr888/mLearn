import knn


def main():
    regression_test = knn.RegressionTest()
    regression_test.load_csv_file('king_county_data_geocoded.csv', 100)
    regression_test.plot_error_rates()


if __name__ == '__main__':
    main()
