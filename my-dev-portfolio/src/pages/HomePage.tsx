import Me from "../components/me";

import meImg from "../assets/img/me.jpeg";
import Timeline from "../components/Timeline";


export default function HomePage() {
  return (
    <>
      <section className="flex flex-col md:flex-row items-center md:items-start md:space-x-6 p-4 center max-w-6xl mx-auto">
        {/* Levý sloupec */}
        <div className="flex-2 mb-6 md:mb-0 ">
          <img src={meImg} alt="Moje foto" className="w-full max-w-sm rounded-lg shadow-lg" />
        </div>

        {/* Pravý sloupec */}
        <div className="flex-1">
          <Me />
        </div>
      </section>

      <section className="p-4 max-w-6xl mx-auto">
        <Timeline />
      </section>

    </>
  );
}
