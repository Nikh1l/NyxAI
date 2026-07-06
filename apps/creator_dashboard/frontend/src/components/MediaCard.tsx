import type { Media } from "../types/instagram";

type Props = {
    media: Media;
};

export default function MediaCard({
    media
}: Props) {
    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: 10,
                overflow: "hidden",
                cursor: "pointer",
            }}
        >
            <img
                src={media.thumbnail_url ?? media.media_url ?? ""}
                alt=""
                style={{
                    width: "100%",
                    aspectRatio: "1",
                    objectFit: "cover"
                }}
            />
            <div style={{ padding: 10 }}>
                <div>
                    {media.caption?.slice(0, 70)}
                </div>
                <small>
                    💬 {media.comments_count}
                </small>
            </div>
        </div>
    )
}