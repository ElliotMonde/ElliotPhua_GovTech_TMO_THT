import React, { useState, useEffect, useRef } from 'react';
import axios from "axios";

export default function Table() {
  const [studentsData, setStudentsData] = useState([]);
  const test = useRef();
  const rerender = React.useReducer(() => ({}), {})[1];
  const getStudentsUrl = "https://elliotphuagovtechtmotht-production.up.railway.app/students";

  useEffect(() => {
    axios
      .get(getStudentsUrl)
      .then(response => {
        setStudentsData(response.data);
        console.log(response);
      })
      .catch((error) => {
        console.error("There was an error fetching the data!", error);
      });
  }, [])
  return (
    <div>
      {studentsData.length > 0 ?
        <table>
          <thead>
            <tr>
              <th>Student Name</th>
              <th>Teacher</th>
              <th>Cumulative GPA</th>
            </tr>
          </thead>
          <tbody>
            {studentsData.map((student, ind) => (
              <tr key={ind}>
                <td>{student.student_name}</td>
                <td>{student.teacher_name}</td>
                <td>{student.cumulative_GPA}</td>
              </tr>
            ))
            }
          </tbody>
          <tfoot>
          </tfoot>
        </table>
        : <p>loading...</p>}
    </div>)
}