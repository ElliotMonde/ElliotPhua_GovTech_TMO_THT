import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import axios from "axios";
import { FormControl, Select, MenuItem, InputLabel, Button, Slider } from '@mui/material';

export default function Table() {
  const [studentsData, setStudentsData] = useState([]);
  const [teachersData, setTeachersData] = useState([]);
  const [newTeacher, setNewTeacher] = useState(false);
  const [checkboxSelection, setCheckBoxSelection] = useState(undefined);
  const baseUrl = "https://elliotphuagovtechtmotht-production.up.railway.app/";
  const getStudentsUrl = baseUrl + "students";
  const getTeachersUrl = baseUrl + "teachers";
  const updateTeacherUrl = baseUrl + `student/${checkboxSelection}`;
  // add checkboxes to allow one selection -> and dropdown to select teacher and button to submit update
  // add draggable range for start and end semester
  // error handling
  // readme -> assumptions
  const getStudents = () => {
    axios
      .get(getStudentsUrl)
      .then(response => {
        setStudentsData(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching students data", error);
      });
  }

  const getTeachers = () => {
    axios
      .get(getTeachersUrl)
      .then(response => {
        setTeachersData(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching teachers data", error)
      });
  }

  const updateTeacher = () => {
    if (checkboxSelection != undefined && newTeacher) {
      axios
        .patch(updateTeacherUrl, { "new_teacher_id": newTeacher })
        .then(response => {
          console.log(response.data);
          getStudents();
        })
        .catch((error) => {
          console.error("There was an error fetching students data", error);
        });
    } else {
      console.log("unable to update teacher." + checkboxSelection + " " + newTeacher);
    }
  }
  useEffect(() => {
    getStudents();
    getTeachers();
  }, [])

  useEffect(() => {
    if (checkboxSelection == undefined) {
      setNewTeacher(false);
    }
  }, [checkboxSelection])

  const columns = [
    { field: 'student_id', headerName: 'ID', width: 75, flex: 1, sortable: true },
    { field: 'student_name', headerName: 'Student Name', width: 240, flex: 2, sortable: true },
    { field: 'teacher_name', headerName: 'Teacher', width: 240, flex: 2, sortable: true },
    { field: 'cumulative_GPA', headerName: 'Cumulative GPA', width: 200, flex: 2, sortable: true }
  ];

  const paginationModel = { page: 0, pageSize: 10 };
  return (
    <>
      <Paper style={{ margin: "70px 70px 20px 70px" }}>
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
      <div style={{ margin: "20px" }}>
        <div>
          <h4>Currently Selected Student: {studentsData.length > 0 && checkboxSelection != undefined ? studentsData[checkboxSelection - 1]["student_name"] : "-"}</h4>
          <h4>Currently Assigned Teacher: {checkboxSelection != undefined ? studentsData[checkboxSelection - 1]["teacher_name"] : "-"}</h4>
        </div>
        <div style={{ display: "flex", flexDirection: "row", justifyContent: "center", marginTop: "50px" }}>
          <h4 style={{ alignContent: "center" }}>Assign New Teacher:</h4>
          <FormControl style={{ margin: "0px 30px", width: "25%" }}>
            <InputLabel id="select-teacher-label">Assign New Teacher</InputLabel>
            <Select
              labelId="select-teacher-label"
              label="Assign New Teacher"
              value={newTeacher ? newTeacher : ""}
              onChange={(e) => { setNewTeacher(e.target.value) }}
              disabled={checkboxSelection === undefined}
            >
              <MenuItem disabled value="">Select</MenuItem>
              {teachersData.length > 0 && teachersData.map((teacher) => {
                return <MenuItem key={teacher["id"]} value={teacher["id"]}>{teacher["name"]}</MenuItem>
              })}
            </Select>
          </FormControl>
          <Button
            variant="contained"
            disabled={checkboxSelection === undefined || !newTeacher}
            onClick={() => {
              updateTeacher();
            }}
          >Submit</Button>
        </div>
      </div>
    </>)
}