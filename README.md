# Example for Muteria in C language.

There are for examples (scenario), each with a corresponding configuration file. Each requires some tools to be installed.

## 1. Using `ctrl/conf.py`

This requires [GNU Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), [Mart](https://github.com/thierry-tct/mart) mutation tool and [KLEE](https://github.com/klee/klee) test generation tool to be installed. Muteria will enable test Generation with KLEE and coverage measurement with Gcov and mutation analysis with Mart.
One may directly run from the following Docker image [https://hub.docker.com/r/thierrytct/klee-semu](https://hub.docker.com/r/thierrytct/klee-semu). An interactive container may be started as following:
```
docker run -it --rm thierrytct/klee-semu bash
```

The analysis can be ran, using the configuration file `ctrl/conf.py`, as following:
```
muteria --config ctrl/conf.py --lang c run
```

## 2. Using `ctrl/conf_semu.py`

This requires [GNU Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), [Mart](https://github.com/thierry-tct/mart) mutation tool and [SEMu](https://github.com/thierry-tct/KLEE-SEMu) mutant test generation tool to be installed. Muteria will enable test Generation with SEMu and coverage measurement with Gcov and mutation analysis with Mart.

One may directly run from the following Docker image [https://hub.docker.com/r/thierrytct/klee-semu](https://hub.docker.com/r/thierrytct/klee-semu). An interactive container may be started as following:
```
docker run -it --rm thierrytct/klee-semu bash
```

The analysis can be ran, using the configuration file `ctrl/conf_semu.py`, as following:
```
muteria --config ctrl/conf_semu.py --lang c run
```

## 3. Using `conf/shadow.py`

This requires [GNU Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), [Mart](https://github.com/thierry-tct/mart) mutation tool and [Shadow](https://srg.doc.ic.ac.uk/files/papers/shadow-icse-16.pdf) patch test generation tool to be installed. Muteria will enable test Generation with SEMu and coverage measurement with Gcov and mutation analysis with Mart.

One may directly run from the following Docker image [https://hub.docker.com/r/thierrytct/cm](https://hub.docker.com/r/thierrytct/cm), Which contains Shadow. The image is built from the repository [https://github.com/thierry-tct/continuous_mutation_docker](https://github.com/thierry-tct/continuous_mutation_docker). An interactive container may be started as following:
```
docker run -it --rm thierrytct/cm bash
```

The analysis can be ran, using the configuration file `ctrl/conf_shadow.py`, as following:
```
muteria --config ctrl/conf_shadow.py --lang c run
```

## 4. Using `conf/shadow_semu.py`
This requires [GNU Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), [Mart](https://github.com/thierry-tct/mart) mutation tool, [SEMu](https://github.com/thierry-tct/KLEE-SEMu) mutant test generation tool and [Shadow](https://srg.doc.ic.ac.uk/files/papers/shadow-icse-16.pdf) patch test generation tool to be installed. Muteria will enable test Generation with SEMu and coverage measurement with Gcov and mutation analysis with Mart.

One may directly run from the following Docker image [https://hub.docker.com/r/thierrytct/cm](https://hub.docker.com/r/thierrytct/cm), Which contains Shadow. The image is built from the repository [https://github.com/thierry-tct/continuous_mutation_docker](https://github.com/thierry-tct/continuous_mutation_docker). An interactive container may be started as following:
```
docker run -it --rm thierrytct/cm bash
```

The analysis can be ran, using the configuration file `ctrl/conf_shadow_semu.py`, as following:
```
muteria --config ctrl/conf_shadow_semu.py --lang c run
```

### TODO
- Add case where we have timeout and segmentation fault (for muteria testing purposes)
- Add a case where the program return a non 0 exit code (for chcking KLEE-REPLAY driver)
