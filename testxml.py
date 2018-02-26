
import urllib
import xml_to_dict

result_path = "http://jenkins.mw.ethan.bskyb.com:8080/job/CI_RUN_DE_AMIDALA_SAT/207/artifact/CI_RUN_DE_AMIDALA_SAT-207/amidala_TEST_005_reset_install_single_lnb_1/output/test_results/TEST-amidala_TEST_005_reset_install_single_lnb.xml"
jsonData = urllib.urlopen(result_path).read()
resultData = xml_to_dict._xml_to_dict(jsonData)['testsuite']

#print resultData
result = {"className": "players_1_action_watchpvr_TEST_030_MalformedWatchPvr",
          "duration": resultData['testcase']['time'],
          "failedSince": resultData['failures'],
          "skipped": "true" if resultData['skipped'] == '1' else "false",
          "stderr": resultData['system-err'],  # stderr",
          "stdout": resultData['system-out'],  # "stdout"#
          }
failure = None

if "failure" in resultData['testcase']:
    print "HIT the failure", resultData['testcase'].keys(),resultData['failures']
    failure = resultData['testcase']['failure']
    print failure
elif "error" in resultData['testcase']:
    print "HIT the error", resultData['testcase'].keys(), resultData['testcase'].keys()
    failure = resultData['testcase']['error']
    print failure
    #sys.exit()

