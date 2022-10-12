
import axios from 'axios';
import { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  //run: uvicorn main:app --reload
  useEffect(() => {axios.get('http://localhost:8000/helloworld').then((res) => {setData(res.data.data1)});}, []);

    return (
      <div>
          <h1 class="text-3xl font-bold underline text-red-400">{data}</h1>
      </div>
    );
  }
  
  export default App;
  