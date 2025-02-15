import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import axios from "axios";
import { FormControl, Select, MenuItem, InputLabel } from '@mui/material';

export default function Table() {
  const [studentsData, setStudentsData] = useState([]);
  const [teachersData, setTeachersData] = useState([]);
  const [checkboxSelection, setCheckBoxSelection] = useState(undefined);
  const baseUrl = "https://elliotphuagovtechtmotht-production.up.railway.app/";
  const getStudentsUrl = baseUrl + "students";
  const getTeachersUrl = baseUrl + "teachers";
  const updateTeacherUrl = baseUrl + `student/${checkboxSelection - 1}`;
  // add checkboxes to allow one selection -> and dropdown to select teacher and button to submit update
  // add draggable range for start and end semester
  // error handling
  // readme -> assumptions
  useEffect(() => {
    axios
      .get(getStudentsUrl)
      .then(response => {
        setStudentsData(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching students data", error);
      });

    axios
      .get(getTeachersUrl)
      .then(response => {
        setTeachersData(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching teachers data", error)
      });
  }, [])

  const columns = [
    { field: 'student_id', headerName: 'ID', width: 75, flex: 1, sortable: true },
    { field: 'student_name', headerName: 'Student Name', width: 240, flex: 2, sortable: true },
    { field: 'teacher_name', headerName: 'Teacher', width: 240, flex: 2, sortable: true },
    { field: 'cumulative_GPA', headerName: 'Cumulative GPA', width: 200, flex: 2, sortable: true }
  ];

  const paginationModel = { page: 0, pageSize: 10 };

  return (
    <>
      <Paper style={{ margin: "70px" }}>
        <DataGrid
          getRowId={(row) => row.student_id}
          rows={studentsData}
          columns={columns}
          initialState={{ pagination: { paginationModel } }}
          pageSizeOptions={[10, 5]}
          checkboxSelection
          disableMultipleRowSelection
          onRowSelectionModelChange={(e) => { setCheckBoxSelection(e[0]) }}
        />
      </Paper>
      <div style={{ margin: "50px" }}>
      <FormControl>
        <InputLabel id="select-teacher-label">Assign New Teacher</InputLabel>
        <Select
          labelId="select-teacher-label"
          value={checkboxSelection != undefined ? studentsData[checkboxSelection - 1]["teacher_name"] : "None"}
          label="Assign New Teacher"
        >
          {teachersData.length > 0 && teachersData.map((teacher, ind) => { 
            <MenuItem value={ teacher["id"]}>{teacher["name"]}</MenuItem>
          })}
        </Select>
        Currently Selected:
        {studentsData.length > 0 && checkboxSelection != undefined ? studentsData[checkboxSelection - 1]["student_name"] : "None"}
        </FormControl>
      </div>
    </>)
}