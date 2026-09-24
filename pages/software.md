---
title: Software
description: Software, toolchains and sensors used in HD mapping, LiDAR, photogrammetry and geodesy production.
keywords:
  - Software
  - Terrasolid
  - Lanelet2
  - Photogrammetry
  - GIS
  - Python
---

# Software & Technical Stack

The toolchain I work in daily, from lane-level HD map production to airborne LiDAR processing, photogrammetry, geodetic control and automation.

---

## Software

| Domain | Tools and methods |
|--------|-------------------|
| HD mapping / AV | **Lanelet2 (OSM)**, JOSM, lane-level network assembly, lane boundaries, virtual and turning lines, intersection cut lines, slicing at condition changes, regulatory associations, GeoJSON layer interchange, QA/QC against automated validation checks, corridor handoff and connectivity, route-stationing tiling specifications |
| Point clouds | **Terrasolid suite** (TerraScan, TerraMatch, TerraModeler, TerraPhoto) on MicroStation and Spatix, TopoDOT, LiDAR360, LAStools, Leica Cyclone 3DR, Trimble RealWorks, strip adjustment, trajectory management, classification and ground filtering, breaklines, DTM/DSM |
| Photogrammetry | **Trimble Inpho** (ApplicationsMaster, UASMaster), ERDAS IMAGINE 16.7 with ORIMA-LPS, Catalyst Professional (PCI Geomatica), Agisoft Metashape, RealityCapture, aerial triangulation, stereo-satellite block adjustment, orthomosaics, SfM, UAV/RPAS |
| Geodesy and GNSS | RTK / PPK / **PPP** (CSRS-PPP, MARGEN, ITRF2020), Trimble Business Center, Leica Infinity, Inertial Explorer, Helmert transformations, site calibration, least-squares network adjustment, geoid QC, CRS/EPSG and datum management, author of the LTM-PTL local projection |
| GIS and remote sensing | **ArcGIS Pro**, QGIS, Global Mapper, Google Earth Engine, eCognition Developer (OBIA and deep learning), NV5 ENVI, PostGIS, GeoServer, spatial databases and SDI, CAD thematic cartography |
| Programming | **Python** (ArcPy, PyQGIS, GDAL/OGR, geospatial libraries), JavaScript (Google Earth Engine), Excel VBA, SQL, PHP, HTML/CSS, AWS EC2 GPU virtual workstations, cloud processing pipelines |
| 3D and visualization | Blender and BlenderGIS, ESRI CityEngine, Unreal Engine (geospatial applications, in progress), geospatial VR/XR, 3D-printing model preparation from DTM/DSM and point clouds, animation rendering |

Licensed in house: Agisoft Metashape and LiDAR360. The rest I work with in client, employer and institutional environments.

---

## Sensors & Field Equipment

| Equipment | Role |
|-----------|------|
| **Leica ALS70-HP / ALS80-HP** with RCD30 metric camera | Airborne sensor operator on 18 campaigns, including the ALS80-HP calibration flight |
| Leica CloudPro, IPAS CO+, FramePro, Inertial Explorer | Airborne LiDAR mission control, trajectory and camera data processing |
| DJI Matrice 300 RTK, Phantom 4 RTK | UAV/RPAS photogrammetric acquisition and training |
| Leica FlexLine TS06 total station, differential GNSS | Ground control, checkpoints and topographic survey |
