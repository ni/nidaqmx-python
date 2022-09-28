"""
 CVI Example program:
    ContPressureBridgeSampleswCal.c

 Example Category:
    AI

 Description:
    This example performs measurements using a Wheatstone
    bridge-based pressure sensor, with bridge calibration (offset
    nulling and shunt calibration) if desired.

 Instructions for Running:
    1. Enter the list of physical channels, and set the attributes
       of the bridge configuration connected to all the channels.
       The 'Maximum Value' and 'Minimum Value' inputs specify the
       range of values that you expect your measurements to return,
       in terms of 'Units'.
    2. Make sure your sensor is in its relaxed state.
    3. You may turn on the 'Do Offset Null?' button to automatically
       null out your sensor's offset by performing a hardware
       nulling operation (if supported by the hardware) followed by
       a software nulling operation. (NOTE: The software nulling
       operation will cause a loss in dynamic range while a hardware
       nulling operation will not cause any loss in the dynamic
       range).
    4. You can turn on the 'Do Shunt Cal?' button to perform a shunt
       calibration (gain adjust calculation) on your sensor. Also,
       specify the shunted value and its location. You must enable
       Offset Null for shunt cal to work correctly. Only enable
       shunt cal if the shunt calibration terminals are connected
       properly.
    5. Specify Sensor Scaling Parameters based on your sensor's data
       sheet or calibration certificate. You can choose to use 'Two
       Point Linear', 'Table', or 'Polynomial' scaling. The
       'Electrical Units' in this section do not have to match the
       'Units' input; if they do not, DAQmx will automatically
       convert the acquired data from 'Electrical Units' to 'Units'.
    - 'Two Point Linear' maps electrical values to physical values
    based on two points. Usually, these points are zero and the
    sensor's capacity, but any two points specified as both
    electrical and physical values will work.
    - 'Table' maps electrical values to physical values based on a
    variable number of points, using linear interpolation. Data that
    would require extrapolating beyond the table endpoints is
    clipped to the closest endpoint.

    - 'Polynomial' uses a set of polynomial coefficients to map from
    electrical values to physical values ('Forward"), or vice versa
    ('Reverse'). Both polynomials are necessary: the forward
    polynomial is used to scale the acquired data, and the reverse
    polynomial is used to select the optimal ADC and amplifier
    settings for the signal range specified by 'Minimum Value' and
    'Maximum Value'. However, this VI only requires you to specify
    one polynomial, and uses the DAQmx Compute Reverse Polynomial
    Coefficients VI to compute the other polynomial.
    6. Run the program and do not disturb your sensor until data
       starts being plotted.

 Steps:
    1. Create an AI Pressure Bridge channel using the desired scale
       type.
    1a. For polynomial scales, use the
    DAQmxCalculateReversePolyCoeff function to compute the other set
    of polynomial coefficients.
    2. Set the rate for the sample clock and set the sample mode to
       Continuous Samples.
    3. Read the sample clock rate property and display the actual
       rate. DAQmx rounds the actual sample clock rate up to the
       next higher supported rate.
    4. If offset nulling is desired, call the
       DAQmxPerformBridgeOffsetNullingCal function to perform both
       hardware nulling (if supported) and software nulling.
    5. If shunt calibration is desired, call the
       DAQmxPerformBridgeShuntCal function. Specify -1 to use the
       bridge resistance that was passed into the
       DAQmxCreateAIBridgeChan function.
    6. Update the stripchart's y-axis label based on the measurement
       units.
    7. Call the DAQmxStartTask function to start the acquisition.
    8. Read the data in the EveryNCallback function until the user
       hits the stop button or an error occurs.
    9. Call the DAQmxStopTask function to stop the acquisition and
       check for errors.
    10. Call the DAQmxClearTask function to clear the Task.
    11. Display an error if any.

 I/O Connections Overview:
     Make sure your signal input terminal matches the Physical
    Channel I/O control. For more detailed connection information,
    refer to your device's hardware reference manual.
"""

#include <ansi_c.h>
#include <stdlib.h>
#include <cvirte.h>
import math
import nidaqmx
from nidaqmx.constants import AcquisitionType
#include <DAQmxIOctrl.h>
#include "ContPressureBridgeSampleswCal.h"

# Input Parameters used for DAQmx channel configuration
phys_channel_names = ['cDAQ1Mod3/ao0', 'cDAQ1Mod3/ao1']
range_max        = 3
range_min        = -3
frequency        = 100
amplitude        = 2
sampsPerCycle    = 40
sampsPerBuffer   = 250
cyclesPerBuffer  = 5
clocksource      = "/cDAQ1/ao/SampleClock"
waveform_types   = ['Triangle', 'Square', 'Sawtooth', 'Sine']
static int panelHandle;

static TaskHandle	gTaskHandle=0;
static float64		*gData=NULL;
static uInt32		gNumChannels;


int32 CVICALLBACK EveryNCallback(TaskHandle taskHandle, int32 everyNsamplesEventType, uInt32 nSamples, void *callbackData);
int32 CVICALLBACK DoneCallback(TaskHandle taskHandle, int32 status, void *callbackData);

int main(int argc, char *argv[])
{
	if( InitCVIRTE(0,argv,0)==0 )
		return -1;  /* out of memory */
	if( (panelHandle=LoadPanel(0,"ContPressureBridgeSampleswCal.uir",PANEL))<0 )
		return -1;
	SetCtrlAttribute(panelHandle,PANEL_DECORATION_BLUE,ATTR_FRAME_COLOR,VAL_BLUE);
	SetCtrlAttribute(panelHandle,PANEL_DECORATION_GREEN,ATTR_FRAME_COLOR,VAL_GREEN);
	SetCtrlAttribute(panelHandle,PANEL_DECORATION_RED,ATTR_FRAME_COLOR,VAL_RED);
	SetCtrlAttribute(panelHandle,PANEL_DECORATION_YELLOW,ATTR_FRAME_COLOR,VAL_YELLOW);
	SetCtrlAttribute(panelHandle,PANEL_DECORATION_WHITE,ATTR_FRAME_COLOR,VAL_WHITE);
	NIDAQmx_NewPhysChanAICtrl(panelHandle,PANEL_CHANNEL,1);
	DisplayPanel(panelHandle);
	RunUserInterface();
	if( gTaskHandle )
		DAQmxClearTask(gTaskHandle);
	DiscardPanel(panelHandle);
	return 0;
}

int CVICALLBACK PanelCallback(int panel, int event, void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_CLOSE )
		QuitUserInterface(0);
	return 0;
}

int CVICALLBACK RangeCallback(int panel, int control, int event, void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT ) {
		double  minVal,maxVal;

		GetCtrlVal(panel,PANEL_MINVAL,&minVal);
		GetCtrlVal(panel,PANEL_MAXVAL,&maxVal);
		if( minVal<maxVal )
			SetAxisScalingMode(panel,PANEL_STRIPCHART,VAL_LEFT_YAXIS,VAL_MANUAL,minVal,maxVal);
		return 1;
	}
	return 0;
}

int CVICALLBACK AddRowCallback (int panel, int control, int event, void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT ) {
		int tabPanel;
		GetPanelHandleFromTabPage(panelHandle,PANEL_TAB,1,&tabPanel);
		InsertTableRows(tabPanel,TABPANEL_1_ELECVALUES,-1,1,VAL_CELL_NUMERIC);
		InsertTableRows(tabPanel,TABPANEL_1_PHYSVALUES,-1,1,VAL_CELL_NUMERIC);
		return 1;
	}
	return 0;
}

int CVICALLBACK DeleteRowCallback (int panel, int control, int event, void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT ) {
		int tabPanel,numTableRows;
		GetPanelHandleFromTabPage(panelHandle,PANEL_TAB,1,&tabPanel);
		GetNumTableRows(tabPanel,TABPANEL_1_ELECVALUES,&numTableRows);
		if (numTableRows<=2)
			return 1;
		else
		{
			DeleteTableRows(tabPanel,TABPANEL_1_ELECVALUES,numTableRows,1);
			DeleteTableRows(tabPanel,TABPANEL_1_PHYSVALUES,numTableRows,1);
			return 1;
		}
	}
	return 0;
}

int CVICALLBACK AddCoefCallback (int panel, int control, int event,
		void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT ) {
		int tabPanel,tabIndex;

		GetActiveTabPage(panelHandle,PANEL_TAB,&tabIndex);
		GetPanelHandleFromTabPage(panelHandle,PANEL_TAB,tabIndex,&tabPanel);
		if (tabIndex==2)
			InsertTableColumns(tabPanel,TABPANEL_2_FORCOEF,-1,1,VAL_CELL_NUMERIC);
		else
			InsertTableColumns(tabPanel,TABPANEL_3_REVCOEF,-1,1,VAL_CELL_NUMERIC);
		return 1;
	}
	return 0;
}

int CVICALLBACK DeleteCoefCallback (int panel, int control, int event,
		void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT ) {
		int tabPanel,tabIndex,numTableColumns;

		GetActiveTabPage(panelHandle,PANEL_TAB,&tabIndex);
		GetPanelHandleFromTabPage(panelHandle,PANEL_TAB,tabIndex,&tabPanel);
		if (tabIndex==2) {
			GetNumTableColumns(tabPanel,TABPANEL_2_FORCOEF,&numTableColumns);
			if (numTableColumns<=1)
				return 1;
			else
				DeleteTableColumns(tabPanel,TABPANEL_2_FORCOEF,numTableColumns,1);
		}
		else {
			GetNumTableColumns(tabPanel,TABPANEL_3_REVCOEF,&numTableColumns);
			if (numTableColumns<=1)
				return 1;
			else
				DeleteTableColumns(tabPanel,TABPANEL_3_REVCOEF,numTableColumns,1);
		}
		return 1;
	}
	return 0;
}

int CVICALLBACK StartCallback(int panel, int control, int event, void *callbackData, int eventData1, int eventData2)
{
	int32       	error=0,strainNull,shuntCal,units,elecUnits,physUnits,samples;
	float64     	minVal,maxVal,rate,actualRate,nominalGageRes,excitationValue,shuntResVal;
	uInt32      	bridgeConfig,excitationSource,shuntResLoc;
	int         	chartLog,tabIndex=0,itemIndex=0;
	char        	chan[256],unitsString[256];
	char        	errBuff[2048]={'\0'};

	if( event==EVENT_COMMIT ) {
		int tabPanel;
		int displaySamples;

		GetCtrlVal(panel,PANEL_CHANNEL,chan);
		GetCtrlVal(panel,PANEL_MINVAL,&minVal);
		GetCtrlVal(panel,PANEL_MAXVAL,&maxVal);
		GetCtrlVal(panel,PANEL_UNITS,&units);
		GetCtrlVal(panel,PANEL_RATE,&rate);
		GetCtrlVal(panel,PANEL_SAMPLES,&samples);
		GetCtrlVal(panel,PANEL_NOMGAGERES,&nominalGageRes);
		GetCtrlVal(panel,PANEL_BRIDGECFG,&bridgeConfig);
		GetCtrlVal(panel,PANEL_EXCSRC,&excitationSource);
		GetCtrlVal(panel,PANEL_EXCVAL,&excitationValue);
		GetCtrlVal(panel,PANEL_STRAIN_NULL,&strainNull);
		GetCtrlVal(panel,PANEL_SHUNT_CAL,&shuntCal);
		GetCtrlVal(panel,PANEL_SHUNTRES,&shuntResVal);
		GetCtrlVal(panel,PANEL_SHUNTLOC,&shuntResLoc);
		GetActiveTabPage(panel,PANEL_TAB,&tabIndex);
		GetPanelHandleFromTabPage(panelHandle,PANEL_TAB,tabIndex,&tabPanel);
		SetCtrlAttribute(panel,PANEL_STRIPCHART,ATTR_XAXIS_GAIN,1.0/rate);
		if (samples>10000)
			displaySamples=10000;
		else
			displaySamples=samples;
		SetCtrlAttribute(panel,PANEL_STRIPCHART,ATTR_POINTS_PER_SCREEN,displaySamples);
		chartLog = (int)log10(rate);
		SetCtrlAttribute(panel,PANEL_STRIPCHART,ATTR_XPRECISION,chartLog);

		/*********************************************/
		// DAQmx Create Channel
		/*********************************************/

		DAQmxErrChk (DAQmxCreateTask("",&gTaskHandle));

		if (tabIndex==1) {
			float64 elecValArray[256],physValArray[256];
			int numRows;

			GetCtrlVal(tabPanel,TABPANEL_1_PHYSUNITS,&physUnits);
			GetCtrlVal(tabPanel,TABPANEL_1_ELECUNITS,&elecUnits);
			GetNumTableRows(tabPanel,TABPANEL_1_ELECVALUES,&numRows);
			GetTableCellRangeVals(tabPanel,TABPANEL_1_ELECVALUES,MakeRect(1,1,numRows,1),elecValArray,VAL_COLUMN_MAJOR);
			GetTableCellRangeVals(tabPanel,TABPANEL_1_PHYSVALUES,MakeRect(1,1,numRows,1),physValArray,VAL_COLUMN_MAJOR);
			DAQmxErrChk (DAQmxCreateAIPressureBridgeTableChan(gTaskHandle,chan,"",minVal,maxVal,units,bridgeConfig,
														excitationSource,excitationValue,nominalGageRes,elecValArray,
														numRows,elecUnits,physValArray,numRows,physUnits,""));
			elecUnits=DAQmx_Val_FromCustomScale;
		}
		else if (tabIndex==2) {
			float64 forCoefArray[256],revCoefArray[256],elecMin=0,elecMax=0;
			int numColumns;

			GetCtrlVal(tabPanel,TABPANEL_2_PHYSUNITS,&physUnits);
			GetCtrlVal(tabPanel,TABPANEL_2_ELECUNITS,&elecUnits);
			GetCtrlVal(tabPanel,TABPANEL_2_ELECMIN,&elecMin);
			GetCtrlVal(tabPanel,TABPANEL_2_ELECMAX,&elecMax);
			GetNumTableColumns(tabPanel,TABPANEL_2_FORCOEF,&numColumns);
			GetTableCellRangeVals(tabPanel,TABPANEL_2_FORCOEF,MakeRect(1,1,1,numColumns),forCoefArray,VAL_ROW_MAJOR);
			DAQmxErrChk (DAQmxCalculateReversePolyCoeff(forCoefArray,numColumns,elecMin,elecMax,1000,-1,revCoefArray));
			DeleteTableColumns(tabPanel,TABPANEL_2_REVCOEF,1,-1);
			InsertTableColumns(tabPanel,TABPANEL_2_REVCOEF,1,numColumns,VAL_CELL_NUMERIC);
			SetTableCellRangeVals(tabPanel,TABPANEL_2_REVCOEF,MakeRect(1,1,1,numColumns),revCoefArray,VAL_ROW_MAJOR);
			DAQmxErrChk (DAQmxCreateAIPressureBridgePolynomialChan(gTaskHandle,chan,"",minVal,maxVal,units,bridgeConfig,
															excitationSource,excitationValue,nominalGageRes,forCoefArray,
															numColumns,revCoefArray,numColumns,elecUnits,physUnits,""));
			elecUnits=DAQmx_Val_FromCustomScale;
		}
		else if (tabIndex==3) {
			float64 forCoefArray[256],revCoefArray[256],physMin,physMax;
			int numColumns;

			GetCtrlVal(tabPanel,TABPANEL_3_PHYSUNITS,&physUnits);
			GetCtrlVal(tabPanel,TABPANEL_3_ELECUNITS,&elecUnits);
			GetCtrlVal(tabPanel,TABPANEL_3_PHYSMIN,&physMin);
			GetCtrlVal(tabPanel,TABPANEL_3_PHYSMAX,&physMax);
			GetNumTableColumns(tabPanel,TABPANEL_3_REVCOEF,&numColumns);
			GetTableCellRangeVals(tabPanel,TABPANEL_3_REVCOEF,MakeRect(1,1,1,numColumns),revCoefArray,VAL_ROW_MAJOR);
			DAQmxErrChk (DAQmxCalculateReversePolyCoeff(revCoefArray,numColumns,physMin,physMax,1000,-1,forCoefArray));
			DeleteTableColumns(tabPanel,TABPANEL_3_FORCOEF,1,-1);
			InsertTableColumns(tabPanel,TABPANEL_3_FORCOEF,1,numColumns,VAL_CELL_NUMERIC);
			SetTableCellRangeVals(tabPanel,TABPANEL_3_FORCOEF,MakeRect(1,1,1,numColumns),forCoefArray,VAL_ROW_MAJOR);
			DAQmxErrChk (DAQmxCreateAIPressureBridgePolynomialChan(gTaskHandle,chan,"",minVal,maxVal,units,bridgeConfig,
															excitationSource,excitationValue,nominalGageRes,forCoefArray,
															numColumns,revCoefArray,numColumns,elecUnits,physUnits,""));
			elecUnits=DAQmx_Val_FromCustomScale;
		}
		else {
			float64 firstElectricalVal,secondElectricalVal,firstPhysicalVal,secondPhysicalVal;

			GetCtrlVal(tabPanel,TABPANEL_0_2NDELECVAL,&secondElectricalVal);
			GetCtrlVal(tabPanel,TABPANEL_0_2NDPHYSVAL,&secondPhysicalVal);
			GetCtrlVal(tabPanel,TABPANEL_0_1STELECVAL,&firstElectricalVal);
			GetCtrlVal(tabPanel,TABPANEL_0_1STPHYSVAL,&firstPhysicalVal);
			GetCtrlVal(tabPanel,TABPANEL_0_PHYSUNITS,&physUnits);
			GetCtrlVal(tabPanel,TABPANEL_0_ELECUNITS,&elecUnits);
			DAQmxErrChk (DAQmxCreateAIPressureBridgeTwoPointLinChan(gTaskHandle,chan,"",minVal,maxVal,units,bridgeConfig,
												excitationSource,excitationValue,nominalGageRes,firstElectricalVal,
												secondElectricalVal,elecUnits,firstPhysicalVal,secondPhysicalVal,
												physUnits,""));
			elecUnits=DAQmx_Val_FromCustomScale;
		}

		GetCtrlIndex(panel,PANEL_UNITS,&itemIndex);
		GetLabelFromIndex(panel,PANEL_UNITS,itemIndex,unitsString);
		SetCtrlAttribute(panel,PANEL_STRIPCHART,ATTR_YNAME,unitsString);

		/*********************************************/
		// DAQmx Configure Code
		/*********************************************/
		SetWaitCursor(1);
		DAQmxErrChk (DAQmxCfgSampClkTiming(gTaskHandle,"",rate,DAQmx_Val_Rising,DAQmx_Val_ContSamps,2*samples));
		DAQmxErrChk (DAQmxGetTaskAttribute(gTaskHandle,DAQmx_Task_NumChans,&gNumChannels));
		DAQmxErrChk (DAQmxGetTimingAttribute(gTaskHandle,DAQmx_SampClk_Rate,&actualRate));
		SetCtrlVal(panel,PANEL_ACTUALRATE,actualRate);

		if( strainNull )
			DAQmxErrChk (DAQmxPerformBridgeOffsetNullingCal(gTaskHandle,""));
		if( shuntCal )
			DAQmxErrChk (DAQmxPerformBridgeShuntCal(gTaskHandle,"",shuntResVal,shuntResLoc,-1,0));

		if( (gData=malloc(samples*gNumChannels*sizeof(float64)))==NULL ) {
			MessagePopup("Error","Not enough memory");
			goto Error;
		}
		SetCtrlAttribute(panel,PANEL_STRIPCHART,ATTR_NUM_TRACES,gNumChannels);
		SetAxisScalingMode(panel,PANEL_STRIPCHART,VAL_LEFT_YAXIS,VAL_MANUAL,minVal,maxVal);

		DAQmxErrChk (DAQmxRegisterEveryNSamplesEvent(gTaskHandle,DAQmx_Val_Acquired_Into_Buffer,samples,0,EveryNCallback,NULL));
		DAQmxErrChk (DAQmxRegisterDoneEvent(gTaskHandle,0,DoneCallback,NULL));

		/*********************************************/
		// DAQmx Start Code
		/*********************************************/
		DAQmxErrChk (DAQmxStartTask(gTaskHandle));

		SetCtrlAttribute(panel,PANEL_START,ATTR_DIMMED,1);
	}

Error:
	SetWaitCursor(0);
	if( DAQmxFailed(error) ) {
		DAQmxGetExtendedErrorInfo(errBuff,2048);
		if( gTaskHandle!=0 ) {
			/*********************************************/
			// DAQmx Stop Code
			/*********************************************/
			DAQmxStopTask(gTaskHandle);
			DAQmxClearTask(gTaskHandle);
			gTaskHandle = 0;

			free(gData);
			gData = NULL;
			SetCtrlAttribute(panel,PANEL_START,ATTR_DIMMED,0);
		}
		MessagePopup("DAQmx Error",errBuff);
	}
	return 0;
}

int CVICALLBACK StopCallback(int panel, int control, int event, void *callbackData, int eventData1, int eventData2)
{
	if( event==EVENT_COMMIT && gTaskHandle ) {
		DAQmxStopTask(gTaskHandle);
		DAQmxClearTask(gTaskHandle);
		gTaskHandle = 0;

		free(gData);
		gData = NULL;
		SetCtrlAttribute(panel,PANEL_START,ATTR_DIMMED,0);
	}
	return 0;
}

int32 CVICALLBACK EveryNCallback(TaskHandle taskHandle, int32 everyNsamplesEventType, uInt32 nSamples, void *callbackData)
{
	int32   error=0;
	char    errBuff[2048]={'\0'};
	int     numRead;

	/*********************************************/
	// DAQmx Read Code
	/*********************************************/
	DAQmxErrChk (DAQmxReadAnalogF64(taskHandle,nSamples,10.0,DAQmx_Val_GroupByScanNumber,gData,nSamples*gNumChannels,&numRead,NULL));
	if( numRead>0 )
		PlotStripChart(panelHandle,PANEL_STRIPCHART,gData,numRead*gNumChannels,0,0,VAL_DOUBLE);

Error:
	if( DAQmxFailed(error) ) {
		DAQmxGetExtendedErrorInfo(errBuff,2048);
		/*********************************************/
		/*/ DAQmx Stop Code
		/*********************************************/
		DAQmxStopTask(taskHandle);
		DAQmxClearTask(taskHandle);
		gTaskHandle = 0;

		free(gData);
		gData = NULL;
		MessagePopup("DAQmx Error",errBuff);
		SetCtrlAttribute(panelHandle,PANEL_START,ATTR_DIMMED,0);
	}
	return 0;
}

int32 CVICALLBACK DoneCallback(TaskHandle taskHandle, int32 status, void *callbackData)
{
	int32   error=0;
	char    errBuff[2048]={'\0'};

	free(gData);
	gData = NULL;
	gTaskHandle = 0;
	// Check to see if an error stopped the task.
	DAQmxErrChk (status);

Error: 
	if( DAQmxFailed(error) ) {
		DAQmxGetExtendedErrorInfo(errBuff,2048); 
	}
	if(taskHandle) {
		DAQmxClearTask(taskHandle); 
	}
	if( DAQmxFailed(error) ) {
		MessagePopup("DAQmx Error",errBuff);
	}
	SetCtrlAttribute(panelHandle,PANEL_START,ATTR_DIMMED,0);
	return 0; 
}