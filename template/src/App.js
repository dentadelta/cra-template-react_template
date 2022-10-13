


import { Chart } from './components/Chart';

function App() {

    return (
      <div className= 'flex flex-col items-center min-h-screen py-2 gap-10'>

          <p className='text-6xl font-bold py-10'>
            Welcome to <span className='text-blue-600'>Power IB!</span>
          </p>
       
      <div className="flex flex-row justify-center min-h-screen md-10 gap-10">
     <Chart csv_file={'chartData.csv'} x_axis={'country'} y_axis={'case'} group_by={'year_month'} filter_by={'filter_column=A'} order_by={'case'} limit={10} chartLabel={"Example Bar"} ChartType={'Bar'}/>
     <Chart csv_file={'chartData.csv'} x_axis={'country'} y_axis={'case'} group_by={'year_month'} filter_by={'filter_column=A'} order_by={'case'} limit={10} chartLabel={"Example Horizontal Bar"} ChartType={'HorizontalBar'}/>
     <Chart csv_file={'chartData.csv'} x_axis={'country'} y_axis={'case'} group_by={'year_month'} filter_by={'filter_column=A'} order_by={'case'} limit={10} chartLabel={"Example Pie"} ChartType={'Pie'}/>
     <Chart csv_file={'chartData.csv'} x_axis={'filter_column'} y_axis={'case'} group_by={'year_month'} filter_by={'filter_column=A'} order_by={'case'} limit={10} chartLabel={"Example Line"} ChartType={'Line'}/>
     </div>
     </div>

    )
  }
  
  export default App;
  
