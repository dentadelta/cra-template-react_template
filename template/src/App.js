
import axios from 'axios';
import { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState({});
  const [arrayData, setArrayData] = useState([]);
  const [dictData, setDictData] = useState({});
  const [urls, setUrls] = useState({});

  //run: uvicorn main:app --reload
  useEffect(() => {axios.get('http://localhost:8000/Appjs').then((res) => {
    setData(res.data.data);
    setArrayData(res.data.dataarray.page_bullet_point);
    setDictData(res.data.datadict.page_dict);
    setUrls(res.data.datadict.url);
  });}, []);

    return (
      <div className="flex flex-col">
      <div className='bg-gray-100'>
        <div className='px-8 py-12 flex flex-row gap-5'>
        <img src={urls.logoUrl} alt='logo' className='h-10 shadow' />
        <h1 className='text-3xl font-bold text-gray-800'>{data.header}</h1>
        </div>
      </div>
      
      <div className='px-8 py-12'>
        <p className='text-2xl text-gray-800'>{data.page_description}</p>
      </div>

      <div className='px-8 py-12'>
          <p className='text-1xl text-gray-800'>{data.page_detail1}</p>
          <ul>
            {arrayData.map((item) => (
                <li>{item}</li>
            ))}
          </ul>
      </div>

      <div className='px-8 py-12'>
          <p className='text-1xl text-gray-800'>{data.page_detail2}</p>
        <ul>
          {Object.keys(dictData).map((key) => (
            <li>{key}: {dictData[key]}</li>
          ))}
        </ul>
        </div>

      </div>

    );
  }
  
  export default App;
  
