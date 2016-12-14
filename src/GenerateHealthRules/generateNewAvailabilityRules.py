__author__ = 'philipp'

import requests

xmlTemplateServiceHealthRule="""
<health-rule>
<name>%%RULENAME%%</name>
<type>OTHER</type>
<description/>
<enabled>true</enabled>
<is-default>false</is-default>
<always-enabled>true</always-enabled>
<duration-min>20</duration-min>
<wait-time-min>30</wait-time-min>
<affected-entities-match-criteria>
<other-affected-entities-match-criteria>
<entity>
<entity-type>APPLICATION</entity-type>
</entity>
</other-affected-entities-match-criteria>
</affected-entities-match-criteria>
<critical-execution-criteria>
<entity-aggregation-scope>
<type>ANY</type>
<value>0</value>
</entity-aggregation-scope>
<policy-condition>
<type>leaf</type>
<display-name>testFailed</display-name>
<condition-value-type>ABSOLUTE</condition-value-type>
<condition-value>2.0</condition-value>
<operator>GREATER_THAN</operator>
<condition-expression/>
<use-active-baseline>false</use-active-baseline>
<metric-expression>
<type>leaf</type>
<function-type>SUM</function-type>
<value>0</value>
<is-literal-expression>false</is-literal-expression>
<display-name>null</display-name>
<metric-definition>
<type>ABSOLUTE_METRIC_SCOPE</type>
<logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|%%TIERNAME%%|Pattern Matches|TestFailed|Count</logical-metric-name>
<metric-name>Custom Metrics|%%EXTENSIONNAME%%|%%TIERNAME%%|Pattern Matches|TestFailed|Count</metric-name>
<entity>
<entity-type>APPLICATION_COMPONENT</entity-type>
<application-component>%%MACHINEAGENTTIER%%</application-component>
</entity>
</metric-definition>
</metric-expression>
</policy-condition>
</critical-execution-criteria>
<warning-execution-criteria>
<entity-aggregation-scope>
<type>ANY</type>
<value>0</value>
</entity-aggregation-scope>
<policy-condition>
<type>leaf</type>
<display-name>statusNotSuccesful</display-name>
<condition-value-type>ABSOLUTE</condition-value-type>
<condition-value>15.0</condition-value>
<operator>LESS_THAN</operator>
<condition-expression/>
<use-active-baseline>false</use-active-baseline>
<metric-expression>
<type>leaf</type>
<function-type>SUM</function-type>
<value>0</value>
<is-literal-expression>false</is-literal-expression>
<display-name>null</display-name>
<metric-definition>
<type>ABSOLUTE_METRIC_SCOPE</type>
<logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|%%TIERNAME%%|Status</logical-metric-name>
<metric-name>Custom Metrics|%%EXTENSIONNAME%%|%%TIERNAME%%|Status</metric-name>
<entity>
<entity-type>APPLICATION_COMPONENT</entity-type>
<application-component>%%MACHINEAGENTTIER%%</application-component>
</entity>
</metric-definition>
</metric-expression>
</policy-condition>
</warning-execution-criteria>
</health-rule>
"""

xmlTemplateServiceGroupHealthRule = """
<health-rule>
        <name>Availability_new_mbbc</name>
        <type>OTHER</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>20</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <other-affected-entities-match-criteria>
                <entity>
                    <entity-type>APPLICATION</entity-type>
                </entity>
            </other-affected-entities-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>boolean</type>
                <operator>OR</operator>
                <condition1>
                    <type>leaf</type>
                    <display-name>dispFailed</display-name>
                    <condition-value-type>ABSOLUTE</condition-value-type>
                    <condition-value>2.0</condition-value>
                    <operator>GREATER_THAN</operator>
                    <condition-expression/>
                    <use-active-baseline>false</use-active-baseline>
                    <metric-expression>
                        <type>leaf</type>
                        <function-type>SUM</function-type>
                        <value>0</value>
                        <is-literal-expression>false</is-literal-expression>
                        <display-name>null</display-name>
                        <metric-definition>
                            <type>ABSOLUTE_METRIC_SCOPE</type>
                            <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_DISP|Pattern Matches|TestFailed|Count</logical-metric-name>
                            <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_DISP|Pattern Matches|TestFailed|Count</metric-name>
                            <entity>
                                <entity-type>APPLICATION_COMPONENT</entity-type>
                                <application-component>%%MACHINEAGENTTIER%%</application-component>
                            </entity>
                        </metric-definition>
                    </metric-expression>
                </condition1>
                <condition2>
                    <type>boolean</type>
                    <operator>OR</operator>
                    <condition1>
                        <type>leaf</type>
                        <display-name>mgmtFailed</display-name>
                        <condition-value-type>ABSOLUTE</condition-value-type>
                        <condition-value>2.0</condition-value>
                        <operator>GREATER_THAN</operator>
                        <condition-expression/>
                        <use-active-baseline>false</use-active-baseline>
                        <metric-expression>
                            <type>leaf</type>
                            <function-type>SUM</function-type>
                            <value>0</value>
                            <is-literal-expression>false</is-literal-expression>
                            <display-name>null</display-name>
                            <metric-definition>
                                <type>ABSOLUTE_METRIC_SCOPE</type>
                                <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_MGMT|Pattern Matches|TestFailed|Count</logical-metric-name>
                                <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_MGMT|Pattern Matches|TestFailed|Count</metric-name>
                                <entity>
                                    <entity-type>APPLICATION_COMPONENT</entity-type>
                                    <application-component>%%MACHINEAGENTTIER%%</application-component>
                                </entity>
                            </metric-definition>
                        </metric-expression>
                    </condition1>
                    <condition2>
                        <type>boolean</type>
                        <operator>OR</operator>
                        <condition1>
                            <type>leaf</type>
                            <display-name>logaccFailed</display-name>
                            <condition-value-type>ABSOLUTE</condition-value-type>
                            <condition-value>2.0</condition-value>
                            <operator>GREATER_THAN</operator>
                            <condition-expression/>
                            <use-active-baseline>false</use-active-baseline>
                            <metric-expression>
                                <type>leaf</type>
                                <function-type>SUM</function-type>
                                <value>0</value>
                                <is-literal-expression>false</is-literal-expression>
                                <display-name>null</display-name>
                                <metric-definition>
                                    <type>ABSOLUTE_METRIC_SCOPE</type>
                                    <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_LOGACC|Pattern Matches|TestFailed|Count</logical-metric-name>
                                    <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_LOGACC|Pattern Matches|TestFailed|Count</metric-name>
                                    <entity>
                                    <entity-type>APPLICATION_COMPONENT</entity-type>
                                    <application-component>%%MACHINEAGENTTIER%%</application-component>
                                    </entity>
                                </metric-definition>
                            </metric-expression>
                        </condition1>
                        <condition2>
                            <type>boolean</type>
                            <operator>OR</operator>
                            <condition1>
                                <type>leaf</type>
                                <display-name>padiFailed</display-name>
                                <condition-value-type>ABSOLUTE</condition-value-type>
                                <condition-value>2.0</condition-value>
                                <operator>GREATER_THAN</operator>
                                <condition-expression/>
                                <use-active-baseline>false</use-active-baseline>
                                <metric-expression>
                                    <type>leaf</type>
                                    <function-type>SUM</function-type>
                                    <value>0</value>
                                    <is-literal-expression>false</is-literal-expression>
                                    <display-name>null</display-name>
                                    <metric-definition>
                                    <type>ABSOLUTE_METRIC_SCOPE</type>
                                    <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_PADI|Pattern Matches|TestFailed|Count</logical-metric-name>
                                    <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_PADI|Pattern Matches|TestFailed|Count</metric-name>
                                    <entity>
                                    <entity-type>APPLICATION_COMPONENT</entity-type>
                                    <application-component>%%MACHINEAGENTTIER%%</application-component>
                                    </entity>
                                    </metric-definition>
                                </metric-expression>
                            </condition1>
                            <condition2>
                                <type>boolean</type>
                                <operator>OR</operator>
                                <condition1>
                                    <type>leaf</type>
                                    <display-name>rucmFailed</display-name>
                                    <condition-value-type>ABSOLUTE</condition-value-type>
                                    <condition-value>2.0</condition-value>
                                    <operator>GREATER_THAN</operator>
                                    <condition-expression/>
                                    <use-active-baseline>false</use-active-baseline>
                                    <metric-expression>
                                    <type>leaf</type>
                                    <function-type>SUM</function-type>
                                    <value>0</value>
                                    <is-literal-expression>false</is-literal-expression>
                                    <display-name>null</display-name>
                                    <metric-definition>
                                    <type>ABSOLUTE_METRIC_SCOPE</type>
                                    <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_RUCM|Pattern Matches|TestFailed|Count</logical-metric-name>
                                    <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_RUCM|Pattern Matches|TestFailed|Count</metric-name>
                                    <entity>
                                    <entity-type>APPLICATION_COMPONENT</entity-type>
                                    <application-component>%%MACHINEAGENTTIER%%</application-component>
                                    </entity>
                                    </metric-definition>
                                    </metric-expression>
                                </condition1>
                                <condition2>
                                    <type>leaf</type>
                                    <display-name>sokoFailed</display-name>
                                    <condition-value-type>ABSOLUTE</condition-value-type>
                                    <condition-value>2.0</condition-value>
                                    <operator>GREATER_THAN</operator>
                                    <condition-expression/>
                                    <use-active-baseline>false</use-active-baseline>
                                    <metric-expression>
                                    <type>leaf</type>
                                    <function-type>SUM</function-type>
                                    <value>0</value>
                                    <is-literal-expression>false</is-literal-expression>
                                    <display-name>null</display-name>
                                    <metric-definition>
                                    <type>ABSOLUTE_METRIC_SCOPE</type>
                                    <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_SOKO|Pattern Matches|TestFailed|Count</logical-metric-name>
                                    <metric-name>Custom Metrics|%%EXTENSIONNAME%%|NEW_MBBC_SOKO|Pattern Matches|TestFailed|Count</metric-name>
                                    <entity>
                                    <entity-type>APPLICATION_COMPONENT</entity-type>
                                    <application-component>%%MACHINEAGENTTIER%%</application-component>
                                    </entity>
                                    </metric-definition>
                                    </metric-expression>
                                </condition2>
                            </condition2>
                        </condition2>
                    </condition2>
                </condition2>
            </policy-condition>
        </critical-execution-criteria>
    </health-rule>
"""

xmlTemplateMachineAvailabilityRule = """
<health-rule>
        <name>Availability_Machine_URLMonitor</name>
        <type>OTHER</type>
        <description/>
        <enabled>true</enabled>
        <is-default>false</is-default>
        <always-enabled>true</always-enabled>
        <duration-min>5</duration-min>
        <wait-time-min>30</wait-time-min>
        <affected-entities-match-criteria>
            <other-affected-entities-match-criteria>
                <entity>
                    <entity-type>APPLICATION</entity-type>
                </entity>
            </other-affected-entities-match-criteria>
        </affected-entities-match-criteria>
        <critical-execution-criteria>
            <entity-aggregation-scope>
                <type>ANY</type>
                <value>0</value>
            </entity-aggregation-scope>
            <policy-condition>
                <type>leaf</type>
                <display-name>machineAvailable</display-name>
                <condition-value-type>ABSOLUTE</condition-value-type>
                <condition-value>4.0</condition-value>
                <operator>LESS_THAN</operator>
                <condition-expression/>
                <use-active-baseline>false</use-active-baseline>
                <metric-expression>
                    <type>leaf</type>
                    <function-type>SUM</function-type>
                    <value>0</value>
                    <is-literal-expression>false</is-literal-expression>
                    <display-name>null</display-name>
                    <metric-definition>
                        <type>ABSOLUTE_METRIC_SCOPE</type>
                        <logical-metric-name>Application Infrastructure Performance|%%MACHINEAGENTTIER%%|Agent|Machine|Availability</logical-metric-name>
                        <metric-name>Agent|Machine|Availability</metric-name>
                        <entity>
                            <entity-type>APPLICATION_COMPONENT</entity-type>
                            <application-component>%%MACHINEAGENTTIER%%</application-component>
                        </entity>
                    </metric-definition>
                </metric-expression>
            </policy-condition>
        </critical-execution-criteria>
    </health-rule>
"""

tiers = [
    "NEW_MBBA_HMIADM", "NEW_MBBA_SPEECH", "NEW_MBBA_SRVADM", "NEW_MBBA_TSSADM", "NEW_MBBA_FBDADM", "NEW_MBBA_PUPADM",
    "NEW_MBBB_ECHO", "NEW_MBBB_NEWS", "NEW_MBBB_FPI", "NEW_MBBB_CITYEV", "NEW_MBBB_PAIR", "NEW_MBBB_PARK", "NEW_MBBB_COUNTR", "NEW_MBBB_FLIGHT", "NEW_MBBB_DESTIM", "NEW_MBBB_CF", "NEW_MBBB_OPR", "NEW_MBBB_OTV","NEW_MBBB_PROFIL","NEW_MBBB_PICNAV","NEW_MBBB_WETTER", "NEW_MBBB_REISE","NEW_MBBB_TWIT", "NEW_MBBB_TRAIN","NEW_MBBB_POI","NEW_MBBB_TRAFFIC", "NEW_MBBB_PRSPOI", "NEW_MBBB_RLU","NEW_MBBB_RS","NEW_MBBB_RUSM", "NEW_MBBB_VSR", "NEW_MBBB_RBC","NEW_MBBB_RPC","NEW_MBBB_RDT","NEW_MBBB_GEOFEN","NEW_MBBB_SPEEDA","NEW_MBBB_RVT","NEW_MBBB_ECALL", "NEW_MBBB_VALETA","NEW_MBBB_EFPI",
    "NEW_MBBC_LOGACC", "NEW_MBBC_PADI", "NEW_MBBC_MGMT", "NEW_MBBC_SOKO", "NEW_MBBC_RUCM", "NEW_MBBC_DISP",
    "NEW_MBBS_SPEECH", "NEW_MBBS_MENUE", "NEW_MBBS_CCSS", "NEW_MBBS_TSS", "NEW_MBBS_APPLST"
]

urls = {
    'createHealthRules': '/controller/healthrules',
}

def createHealthRule(schema, server, port, user, password, application):
    params = { "overwrite" : "true" }
    files = {'file': ('fileUpload', open('xmlExport.xml', 'rb'), 'application/xml', {'Expires': '0'})}
    r = requests.post(schema + "://" + server + ":" + port + urls['createHealthRules'] + "/" + str(application), params=params, auth=(user, password), files=files)
    return r._content

def getHealthRule(machineAgentTier, tier, extensionName, ruleName):
    hr = xmlTemplateServiceHealthRule.replace("%%MACHINEAGENTTIER%%", machineAgentTier).replace("%%TIERNAME%%", tier).replace("%%EXTENSIONNAME%%", extensionName).replace("%%RULENAME%%", ruleName)
    return hr

def getHealthRuleGroup(machineAgentTier, extensionName):
    hr = xmlTemplateServiceGroupHealthRule.replace("%%MACHINEAGENTTIER%%", machineAgentTier).replace("%%EXTENSIONNAME%%", extensionName)
    return hr

def getMachineRule(machineAgentTier):
    hr = xmlTemplateMachineAvailabilityRule.replace("%%MACHINEAGENTTIER%%", machineAgentTier)
    return hr

def getRulXMLHeader():
    return "<health-rules controller-version='004-000-008-003'>"

def getRuleXMLFooter():
    return "</health-rules>"

machineAgentTier = "AppDynamicsVM"
extensionName = "URL Monitor"
server= "localhost"
port = "7090"
user = "admin@customer1"
password = "AppDyn#2015"
xmlExportFile = open("xmlExport.xml", 'w')
xmlExportFile.truncate()
xmlExportFile.write(getRulXMLHeader())
xmlExportFile.write("\n")
for tier in tiers:
    hr = getHealthRule(machineAgentTier, tier, extensionName, "Availability_" + tier.lower())
    xmlExportFile.write(hr)
    xmlExportFile.write("\n")
xmlExportFile.write(getHealthRuleGroup(machineAgentTier,extensionName))
xmlExportFile.write("\n")
xmlExportFile.write(getMachineRule(machineAgentTier))
xmlExportFile.write("\n")
xmlExportFile.write(getRuleXMLFooter())
xmlExportFile.close()

response = createHealthRule("http", server, port, user, password, 4)
print (response)

