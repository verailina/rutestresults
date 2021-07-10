# rutestresults

## Installation

```bash
cd rutestresults
pip install .
```

Use `pip install -e .` to be able to modify and execute the code without reinstallation.

## Commands

After installation, two commands are available:

* ```show-test-results```

  Command `show-test-results` generates `chart.html` file with resulting plots.


* ```load-test-results```

  Command `load-test-results` outputs a head of preprocessed dataframe.
  
  Example output:
```Loading
                                name      total  Math  Russian     IT program  Foreign language
0         Абрамов Петр Александрович        243  75.0     98.0   70.0     itb               NaN
1       Амерханова Наргиза Артуровна        286  96.0     89.0   96.0     itb               NaN
2         Баранов Алексей Алексеевич        235  45.0     96.0   94.0     itb               NaN
```
