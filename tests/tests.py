import sys, os

import numpy as np

import troia
from tdpy import summgene


def cnfg_prev():
    '''
    Previous discoveries
    '''    
    
    dictmileinpt = dict()
    dictmileinpt['dictpboxinpt'] = dict()
    dictmileinpt['dictpboxinpt']['factosam'] = 0.1

    troia.init( \
               typesyst='cosc', \
               liststrgmast=['V723 Mon', 'VFTS 243', 'HR 6819', 'A0620-00'], \
               typeinst='TESS', \
               typepopl='prev', \
               dictmileinpt=dictmileinpt, \
              )

    
def cnfg_TESSGEO():
    '''
    Simulated analysis for simulatenaous data collected by TESS EM2 and TESS L5
    '''
    
    troia.init( \
               typesyst='cosc', \
               typeinst='TESS-GEO', \
               typepopl='targtess_prms_2min', \
               typedata='simutoyy', \
               booldiag=True, \
              )


def cnfg_candidates_Rom():
    '''
    Targets from Rom's RNN
    '''
    
    dictmileinpt = dict()
    dictmileinpt['dictlcurtessinpt'] = {'typelcurtpxftess': 'SPOC'}
    
    listticitarg = [21266729, 14397653, 12967420, 3892500, 3664978, 1008024, 1066665, 2761086, 3542993]
    troia.init( \
               typesyst='cosc', \
               listticitarg=listticitarg, \
               typepopl='candidates_Rom', \
               dictmileinpt=dictmileinpt, \
               typeinst='TESS', \
              )


def cnfg_XRB():
    '''
    XRBs in Kartik's catalog
    '''

    troia.init( \
               typesyst='cosc', \
               liststrgmast=['HR6819', 'Vela X-1'], \
               typepopl='XRB', \
              )


def cnfg_TargetsOfInterest():
    
    # black hole candidate from Eli's list
    listticitarg = [281562429]
    # Rafael
    listticitarg = [356069146]


def cnfg_rvel():
    '''
    High RV targets from Gaia DR2
    '''   
    
    troia.init( \
               typesyst='cosc', \
               typepopl='rvel', \
              )


def cnfg_tessnomi2min(typedata='simutoyy'):
    '''
    2-minute targets from the nominal mission
    '''
    
    dictmileinpt = dict()
    dictmileinpt['dictpboxinpt'] = dict()
    #dictmileinpt['dictpboxinpt']['factosam'] = 1.
    #dictmileinpt['dictpboxinpt']['minmperi'] = 5.394
    #dictmileinpt['dictpboxinpt']['maxmperi'] = 5.402
    
    # oversampling factor (wrt to transit duration) when rebinning data to decrease the time resolution
    dictmileinpt['dictpboxinpt']['factduracade'] = 2.
    # factor by which to oversample the frequency grid
    dictmileinpt['dictpboxinpt']['factosam'] = 10.
    # number of duty cycle samples  
    dictmileinpt['dictpboxinpt']['numbdcyc'] = 3
    # spread in the logarithm of duty cycle
    dictmileinpt['dictpboxinpt']['deltlogtdcyc'] = 0.5
    # epoc steps divided by trial duration
    dictmileinpt['dictpboxinpt']['factdeltepocdura'] = 0.5

    dictlcurtessinpt = dict()
    dictlcurtessinpt['booltpxfonly'] = True
    
    troia.init( \
               typesyst='cosc', \
               typeinst='TESS', \
               typepopl='targtess_prms_2min', \
               typedata=typedata, \
               dictmileinpt=dictmileinpt, \
               booldiag=True, \
               dictlcurtessinpt=dictlcurtessinpt, \
              )


def cnfg_cycle3_G03254():
    '''
    Targets in TESS GI Cycle 3 proposal (PI: Tansu Daylan, G03254)
    '''
    
    path = os.environ['TROIA_DATA_PATH'] + '/data/G03254_Cycle3_GI.csv'
    objtfile = open(path, 'r')
    listticitarg = []
    k = 0
    for line in objtfile:
        if k != 0 and not line.startswith('#') and line != '\n':
            strgtici = line.split(',')[0]
            listticitarg.append(strgtici)
        k += 1
        if len(listticitarg) == 10:
            break
    listticitarg = np.array(listticitarg)
    listticitarg = listticitarg.astype(int)
    listticitarg = np.unique(listticitarg)
    troia.init( \
               typesyst='cosc', \
               typepopl='cycle3_G03254', \
               listticitarg=listticitarg, \
               typeinst='TESS', \
              )


globals().get(sys.argv[1])(*sys.argv[2:])