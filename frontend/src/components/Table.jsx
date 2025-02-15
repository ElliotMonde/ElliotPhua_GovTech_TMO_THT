import React, { useState, useEffect } from 'react';
import axios from "axios";

export default function Table() {
  const [studentsData, setStudentsData] = useState([]);
  const [error, setError] = useState(null);
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
        setError("Failed to fetch students data");
        console.error("There was an error fetching the data!", error);
      });
  }, [])
  return (
    <div>
      { studentsData }
    </div>
  )
}