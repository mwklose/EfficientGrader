/*****
Question 1: Heart Data
 *****/
PROC PRINT DATA=SASHELP.HEART (OBS=10);

RUN;

/*****
Question 2: Infant Data
 *****/
PROC FREQ DATA=SASHELP.BIRTHWGT;

    TABLES LowBirthWgt*AgeGroup;
    
RUN; 