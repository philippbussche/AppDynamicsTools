#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'philipp'

from controller_handler import ControllerHandler
import json
import re

ch = ControllerHandler("https",
                       "asdasdasd",
                       "443",
                       "asdadasd",
                       True)

blacklistPatterns = ["(?i).*bupa.*"]
useWhitelist = True
whitelistPatterns = ["(?i).*prod-bootstrap.*"]
limitMetrics = True
metricLimit = 3
metricCounter = 0

analytics_metrics = ch.getAnalyticsScheduledQueryReports()

# print json.dumps(analytics_metrics, sort_keys=True, indent=4 )

def prefix_query_name(query, prefix):
    return prefix + "-" + query

def replace_query(query, old, new):
    return query.replace(old, new)

for metric in analytics_metrics:
    if (limitMetrics is False) or (limitMetrics is True and metricCounter < metricLimit):
        print "Processing metric with name: " + metric['queryName']
        for pattern in blacklistPatterns:
            m = re.search(pattern, metric['queryName'])
            if m:
                print "--> Metric blacklisted so not further processing it."
            else:
                if useWhitelist is False or (useWhitelist is True and any(re.search(whitelistPattern, metric['queryName']) for whitelistPattern in whitelistPatterns)):
                    if "PROD" in metric['queryName']:
                        print "--> I have to copy this metric, change PROD to STAG in the name as well as adjust the ADQL."
                        if metric['adqlQueryString'] is None:
                            print "--> Can't recreate metric with name '" + metric['queryName'] + "' using query string since is Null."
                            if "PROD" in metric['rawQueryString']:
                                print "--> Found reference to PROD in rawQueryString, trying to re-create metric just using the rawQueryString"
                                adjusted_rawQueryString = replace_query(metric['rawQueryString'], 'PROD', 'STAG')
                                new_metric_name = replace_query(metric['queryName'], 'PROD', 'STAG')
                                parent_metric_name = metric['queryName']
                                if metric['queryDescription']:
                                    parent_metric_description = replace_query(metric['queryDescription'], 'PROD', 'STAG')
                                else:
                                    parent_metric_description = "n/a"
                                print "----> New metric name is: " + new_metric_name
                                print "----> New raw AQDL query is: " + adjusted_rawQueryString
                                # ch.createNewAnalyticsMetric(new_metric_name, 'rawQueryString', adjusted_rawQueryString, parent_metric_name, parent_metric_description)
                                # metricCounter += 1
                                print "------> However not creating this metric as we know at the moment that this would not work with the REST call we are using."
                            else:
                                print "----> There is no reference to PROD in rawQueryString hence not re-creating it for STAG."
                        else:
                            if "PROD" in metric['adqlQueryString']:
                                adjusted_adql = replace_query(metric['adqlQueryString'], 'PROD', 'STAG')
                                new_metric_name = replace_query(metric['queryName'], 'PROD', 'STAG')
                                # if new_metric_name not in analytics_metrics['queryName']:
                                if not any(new_metric_name == m['queryName'] for m in analytics_metrics):
                                    parent_metric_name = metric['queryName']
                                    if metric['queryDescription']:
                                        parent_metric_description = replace_query(metric['queryDescription'], 'PROD', 'STAG')
                                    else:
                                        parent_metric_description = "n/a"
                                    print "----> New metric name is: " + new_metric_name
                                    print "----> New AQDL query is: " + adjusted_adql
                                    ch.createNewAnalyticsMetric(new_metric_name, 'adqlQueryString', adjusted_adql, parent_metric_name, parent_metric_description)
                                    metricCounter += 1
                                else:
                                    print "------> A metric with this name already exists, hence not re-creating it."
                            else:
                                print "----> There is no reference to PROD in adqlQueryString hence not re-creating it for STAG."
                    elif "STAG" in metric['queryName']:
                        print "--> I don't have to do anything with this metric."
                    else:
                        print "--> I have to copy this metric, add STAG to the name as well as adjust the ADQL."
                        if metric['adqlQueryString'] is None:
                            print "--> Can't recreate metric with name '" + metric['queryName'] + "' using query string since is Null."
                            if "PROD" in metric['rawQueryString']:
                                print "--> Found reference to PROD in rawQueryString, trying to re-create metric just using the rawQueryString"
                                adjusted_rawQueryString = replace_query(metric['rawQueryString'], 'PROD', 'STAG')
                                new_metric_name = prefix_query_name(metric['queryName'], 'STAG')
                                parent_metric_name = metric['queryName']
                                if metric['queryDescription']:
                                    parent_metric_description = replace_query(metric['queryDescription'], 'PROD', 'STAG')
                                else:
                                    parent_metric_description = "n/a"
                                print "----> New metric name is: " + new_metric_name
                                print "----> New raw AQDL query is: " + adjusted_rawQueryString
                                # ch.createNewAnalyticsMetric(new_metric_name, 'rawQueryString', adjusted_rawQueryString, parent_metric_name, parent_metric_description)
                                # metricCounter += 1
                                print "------> However not creating this metric as we know at the moment that this would not work with the REST call we are using."
                            else:
                                print "----> There is no reference to PROD in rawQueryString hence not re-creating it for STAG."
                        else:
                            if "PROD" in metric['adqlQueryString']:
                                new_metric_name = prefix_query_name(metric['queryName'], 'STAG')
                                adjusted_adql = replace_query(metric['adqlQueryString'], 'PROD', 'STAG')
                                if not any(new_metric_name == m['queryName'] for m in analytics_metrics):
                                    parent_metric_name = metric['queryName']
                                    if metric['queryDescription']:
                                        parent_metric_description = replace_query(metric['queryDescription'], 'PROD', 'STAG')
                                    else:
                                        parent_metric_description = "n/a"
                                    print "----> New metric name is: " + new_metric_name
                                    print "----> New AQDL query is: " + adjusted_adql
                                    ch.createNewAnalyticsMetric(new_metric_name, 'adqlQueryString', adjusted_adql, parent_metric_name, parent_metric_description)
                                    metricCounter += 1
                                else:
                                    print "------> A metric with this name already exists, hence not re-creating it."
                            else:
                                print "----> There is no reference to PROD in adqlQueryString hence not re-creating it for STAG."
                else:
                    print "--> Metric whitelisting ative but metric not whitelisted so not processing it."
    elif limitMetrics is True and metricCounter >= metricLimit:
        print "Can't process any more metrics as we just have hit the configured metric limit."
        print "Metric limit was set to: " + str(metricLimit)
        break

print "Number of created metrics: " + str(metricCounter)
