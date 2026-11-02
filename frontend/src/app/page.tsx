import Hero from "./components/Hero";
export default function Home() {
  return (
    
    <div className="flex flex-col gap-5  items-center text-white justify- bg-white font-sans ">
      <Hero/>
       
      <div className="flex flex-row gap-10 ">
        <div className="h-40 w-40 hover:w-[400px] hover:h-[300px] transition-all duration-700 ease-in-out rounded bg-black"></div>
      </div> 
      <div className="flex flex-row gap-10 ">
        <div className="h-40 w-40 hover:w-[400px] hover:h-[300px] transition-all duration-700 ease-in-out rounded bg-black"></div>
      </div> 
      <div className="flex flex-row gap-10 ">
        <div className="h-40 w-40 hover:w-[400px] hover:h-[300px] transition-all duration-700 ease-in-out rounded bg-black"></div>
      </div> 
     
      
      
      </div>
  );
}

