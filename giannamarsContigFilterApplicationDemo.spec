/*
A KBase module: giannamarsContigFilterApplicationDemo
This sample module contains one small method that filters contigs.
*/

module giannamarsContigFilterApplicationDemo {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_giannamarsContigFilterApplicationDemo(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
