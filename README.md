Example for Muteria

- THis requires [GNU Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), [Mart](https://github.com/thierry-tct/mart) mutation tool and [KLEE](https://github.com/klee/klee) test generation tool to be installed.
- run using the configuration file in `ctrl/conf.py`.
- `muteria --config ctrl/conf.py --lang c run`

Additionally, to use shadow symbolic execution for check test generation, use `conf_shadow.py`

## TODO
- Add case where we have timeout and segmentation fault (for muteria testing purposes)
- Add a case where the program return a non 0 exit code (for chcking KLEE-REPLAY driver)
