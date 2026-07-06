import MediaCard  from "./MediaCard";
import { useMedia } from "../hooks/useMedia";

export default function MediaGrid() {

    const { data, isLoading } = useMedia();

    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    return (
        <div
            style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
                gap: 20,
            }}
        >
            {data?.map((media) => (
                <MediaCard
                    key={media.id}
                    media={media}
                />
            ))}
        </div>
    )
}