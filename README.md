# feature glossary
* **PTEGENDER**: biological sex - female (0) and male (1) 
* **PTEDUCAT**: duration of education in years
* **AGE**: age in years 
* **APOE2**: gene dosage of apolipoprotein (APOE) ε2 alleles, ranging from 0 to 2
* **APOE4**: gene dosage of APOE ε4 alleles, ranging from 0 to 2
* **MMSE**: mini-mental state examination 
* **CATANIMSC**: category fluency (animals) test
* **TRABSCOR**: Trail Making Testing Part B 
* **LDELTOTAL**: logical memory delayed recall test scores from Weschler Memory Scale-Revised or Weschler Memory Scale III
* **BMI**: body mass index 
* **RATIO_ABETA42_40_BY_ISTD_TOUSE**: plasma Aβ42/Aβ40 ratio measured by a high-precission mass spectrometry assay (more details at https://n.neurology.org/content/93/17/e1647)
* *volumes and surfaces of regions of interest (ROIs) in structural MRI scans*: 
  * follow the naming conventions of FastSurfer (GitHub: https://github.com/Deep-MI/FastSurfer paper: https://www.sciencedirect.com/science/article/pii/S1053811920304985)
  * normalize ROI volumes to the total intracranial volume

# instructions for running predictions

## set up Pythron environment
* Python >3.0 is required 
* ```requirements.txt``` contains a list of dependencies

## prepare input (```.csv```) file
For each feature subset, refer to ```example_input.csv``` in ```/models``` for how the input file shoudl be formated. Note that the column names and the order in which they appear must exactly match ```example_input.csv```.

## run prediction script with required arguments 
```python predict.py```
* ```-i```: input path (```.csv```) that contains the biomarkers for prediction
* ```-o```: output path (```.csv```) where prediction results will be saved
* ```-f```: feature subset
  * ```0```: demographic, BMI, genetic, cognitive, and MRI biomarkers
  * ```1```: demographic, BMI, genetic, and cognitive biomarkers
  * ```2```: demographic, BMI, and genetic biomarkers
  * ```3```: demographic, BMI, and cognitive biomarkers
  * ```p```: demographic, BMI, genetic, cognitive, and plasma biomarkers
* ```-m```: type of logical memory delayed recall test (only need to be specified if ```-f``` is ```0```, ```1```, ```3```, or ```p```)
  * ```r```: Wechsler Memory Scale-Revised Logical Memory Delayed, ranging from 0 - 25
  * ```3```: Wechsler Memory Scale III Logical Memory Delayed, ranging from 0 - 50