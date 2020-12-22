import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conf_shadow import *
sys.path.pop(0)

ENABLED_CRITERIA = []
from muteria.drivers.testgeneration.tools_by_languages.c.semu.driver_config \
                                             import MetaMuSource, DriverConfigSemu
distance = 10
pre_flags = [
                                ('-semu-checkpoint-window', str(distance)),
                                ('-semu-minimum-propagation-depth', '0'),
                                ('-semu-propagation-proportion', '0.0'),
                                ('-semu-precondition-length', '-2'), # start from top
                                #('-semu-max-total-tests-gen', '1000')
                                ('-semu-number-of-tests-per-mutant', '500000'),
                                ('-solver-backend', 'z3'),
                                ('-max-memory', '150000'),
                                
                                #('-semu-no-state-difference',),
                                #('-semu-MDO-propagation-selection-strategy',),
                                #('-semu-use-basicblock-for-distance',),
                                ('-semu-forkprocessfor-segv-externalcalls',),
                                #('-semu-testsgen-only-for-critical-diffs',),
                                #('-semu-no-environment-output-diff',),

                                #('-seed-out-dir', "/work_data/cr-22/ktests_seeds"),
                            ]
semu_test_cmp = TestcaseToolsConfig(tooltype=TestToolType.USE_CODE_AND_TESTS, \
                        toolname='semu', \
                        tool_user_custom=ToolUserCustom(
                            PRE_TARGET_CMD_ORDERED_FLAGS_LIST=pre_flags,
                            POST_TARGET_CMD_ORDERED_FLAGS_LIST=[('-sym-args', '2', '2', '2')],
                            DRIVER_CONFIG = DriverConfigSemu(meta_mutant_source=MetaMuSource.ANNOTATION, verbose_generation=True),
                        )
                     )

TESTCASE_TOOLS_CONFIGS = [semu_test_cmp, dev_test]
